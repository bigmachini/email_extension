import smtplib, ssl
import sys

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import configparser
import logging.config
import logging
import os

ENCRYPTION_TYPE = ['SSL', 'TLS']


class EmailHelper:

    def __init__(self, _smtp_server=None, _port=None, _encryption_type=None, _username=None, _password=None,
                 _config_filename=None):
        msg = []
        if not _smtp_server:
            msg.append('SMTP_SERVER_REQUIRED')
        if not _port:
            msg.append('PORT_REQUIRED')
        if not _username:
            msg.append('USERNAME_REQUIRED')
        if not _password:
            msg.append('PASSWORD_REQUIRED')
        if not _config_filename:
            msg.append('CONFIGURATION_FILE_REQUIRED')
        if not _encryption_type:
            msg.append('ENCRYPTION_TYPE_REQUIRED')
            if _encryption_type not in ENCRYPTION_TYPE:
                msg.append('INVALID_ENCRYPTION_TYPE_REQUIRED')

        if msg:
            raise Exception(msg)

        self.smtp_server = _smtp_server
        self.port = _port
        self.username = _username
        self.password = _password
        self.encryption_type = _encryption_type
        self.config, self.logger = self.get_config(_config_filename)
        self.logger.info('smtp_server: {} port: {} username: {}  encryption_type: {}'.format(
            _smtp_server,
            _port,
            _username,
            _encryption_type
        ))

    def get_config(self, _filename='settings.ini'):
        config_parser = configparser.ConfigParser()
        _config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), ".", _filename))

        # self.d = config_parser.read(_config_file)
        logging.config.fileConfig(_config_file)

        logger = logging.getLogger(__name__)
        return config_parser, logger

    def email(self, _to, _subject, _body, _subtype='plain', _from=None, _cc=None, _bcc=None, _file_path=None,
              _filename=None):
        msg = []
        if not _to:
            msg.append('RECEIVER_REQUIRED')
        if not _subject:
            msg.append('SUBJECT_REQUIRED')
        if not _body:
            msg.append('BODY_REQUIRED')

        if msg:
            raise Exception(msg)

        message = MIMEMultipart()
        if not _from:
            _from = self.username

        message["From"] = _from
        message["To"] = _to
        message["Subject"] = _subject
        if _cc:
            message["cc"] = _cc
        if _bcc:
            message["Bcc"] = _bcc  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(_body, _subtype))

        if _file_path:
            # Open PDF file in binary mode
            with open(_file_path, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            if not _filename:
                _filename = 'attachment'
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {_filename}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        try:
            context = ssl.create_default_context()
            if self.encryption_type == ENCRYPTION_TYPE[0]:
                with smtplib.SMTP(smtp_server, port) as server:
                    server.starttls(context=context)
                    server.login(self.username, self.password)
                    server.sendmail(_from, _to, text)
            if self.encryption_type == ENCRYPTION_TYPE[1]:
                with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
                    server.login(self.username, self.password)
                    server.sendmail(_from, _to, text)
        except Exception as ex:
            print("Ex: {}".format(ex))
            self.logger.exception(ex)


if __name__ == '__main__':

    if len(sys.argv) < 8:
        print(
            "python email_helper [smtp_server] [port] [username] [password] [to] [encryption_type] [config_filename] [attachment_path]")
    else:
        port = sys.argv[2]
        password = sys.argv[4]
        username = sys.argv[3]
        smtp_server = sys.argv[1]
        receiver_email = sys.argv[5]
        encryption_type = sys.argv[6]
        config_file = sys.argv[7]

        if len(sys.argv) == 9:
            filename = sys.argv[8]  # './data/data.csv'

        email_helper = EmailHelper(smtp_server, port, encryption_type, username, password, config_file)
        _config, _logger = email_helper.get_config()

        if len(sys.argv) == 9:
            filename = sys.argv[8]  # './data/data.csv'
            email_helper.email(receiver_email, 'Testing Subject {} attachment'.format(encryption_type), 'Testing Body',
                               _filename='attachment.ini', _file_path=filename)
        else:
            email_helper.email(receiver_email, 'Testing Subject {}'.format(encryption_type), 'Testing Body')
