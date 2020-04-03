import smtplib, ssl
import sys

import configparser
import logging.config

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import logging
import os


def get_extension(_path):
    return _path.split('.')[-1]


ENCRYPTION_TYPE = ['SSL', 'TLS']
SUBTYPE = ['plain', 'html']


def get_config(_filename='settings.ini'):
    path = os.environ["EE_CONFIG"]
    config_parser = configparser.ConfigParser()
    _config_file = "{}/{}".format(path, _filename)
    config_parser.read(_config_file)
    logging.config.fileConfig(_config_file)
    logger = logging.getLogger(__name__)
    return config_parser, logger


def get_email_by_path(_filename):
    with open(_filename) as f:
        return f.readlines()


class EmailHelper:

    def __init__(self, _smtp_server=None, _port=None, _encryption_type=None, _username=None, _password=None,
                 _logger=None):
        msg = []
        if not _smtp_server:
            msg.append('SMTP_SERVER_REQUIRED')
        if not _port:
            msg.append('PORT_REQUIRED')
        if not _username:
            msg.append('USERNAME_REQUIRED')
        if not _password:
            msg.append('PASSWORD_REQUIRED')
        if not _logger:
            msg.append('LOGGER_REQUIRED')
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
        self.logger = _logger

        self.logger.info('smtp_server: {} port: {} username: {}  encryption_type: {}'.format(
            _smtp_server,
            _port,
            _username,
            _encryption_type
        ))

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
            _ext = get_extension(_file_path)
            if not _filename:
                _filename = 'attachment.{}'.format(_ext)
            else:
                _filename = '{}.{}'.format(_filename.split('.')[0], _ext)

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
            if self.encryption_type == 'SSL':
                with smtplib.SMTP(self.smtp_server, self.port) as server:
                    server.starttls(context=context)
                    server.login(self.username, self.password)
                    res = server.sendmail(_from, _to, text)
                    self.logger.info("response-{}: {}".format(self.encryption_type, res))
            if self.encryption_type == 'TLS':
                with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
                    server.login(self.username, self.password)
                    res = server.sendmail(_from, _to, text)
                    self.logger.info("response-{}: {}".format(self.encryption_type, res))
        except Exception as ex:
            self.logger.exception(ex)
