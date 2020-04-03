"""Read the latest Real Python tutorials
Usage:
------
    $ emailext [to] [config_filename] [email_path] [email_type] [attachment_path] [attachment_name]

Send Email Without attachement:
    $ emailext <receiver_email> <config_filename> <email_path> <email_type>

Send Email Without attachement:
    $ emailext <receiver_email> <config_filename> <email_path> <email_type>  <attachment_path> <attachment_name>

Available options are:
    -h, --help         Show this help
    -l, --show-links   Show links in text
Contact:
--------
- https://realpython.com/contact/
More information is available at:
- https://pypi.org/project/realpython-reader/
- https://github.com/realpython/reader
Version:
--------
- realpython-reader v1.0.0
"""

import sys
from email_extension.email_helper import EmailHelper, ENCRYPTION_TYPE, SUBTYPE, get_config


def main():
    if len(sys.argv) > 1:
        if len(sys.argv) < 3:
            raise Exception(
                'wrong format: use python __main__.py [to] [config_filename] '
                '[email_path] [email_type]  [attachment_path] [attachment_name]')
        else:
            receiver_email = sys.argv[1]
            config_file = sys.argv[2]

            config_parser, logger = get_config(config_file)
            port = config_parser.get('email', 'port')
            password = config_parser.get('email', 'password')
            username = config_parser.get('email', 'username')
            smtp_server = config_parser.get('email', 'smtp_server')
            encryption_type = config_parser.get('email', 'encryption_type')
            if encryption_type not in ENCRYPTION_TYPE:
                raise Exception(
                    'invalid encryption type. [SSL/TLS]')

            email_helper = EmailHelper(smtp_server, port, encryption_type, username, password, logger)
            message = 'Test Body'
            subtype = 'plain'

            _filename = None
            _file_path = None

            # check if users has entered email path and subtype
            if len(sys.argv) > 3:
                _msg_path = _file_path = sys.argv[3]
                subtype = _file_path = sys.argv[4]

                if subtype not in SUBTYPE:
                    raise Exception(
                        'invalid subtype. [plain/html]')

                if len(sys.argv) > 6:
                    _file_path = sys.argv[5]  # './data/data.csv'

                    if len(sys.argv) == 7:
                        _filename = sys.argv[6]
                    subject = 'Testing Subject {} attachment'.format(encryption_type)
            else:
                subject = 'Testing Subject {} no attachment'.format(encryption_type)

            email_helper.email(receiver_email, subject, message,
                               _file_path=_file_path,
                               _filename=_filename,
                               _subtype=subtype)
    else:
        config_parser, logger = get_config('settings.ini')
        port = config_parser.get('email', 'port')
        password = config_parser.get('email', 'password')
        username = config_parser.get('email', 'username')
        smtp_server = config_parser.get('email', 'smtp_server')
        encryption_type = config_parser.get('email', 'encryption_type')
        EmailHelper(smtp_server, port, encryption_type, username, password, logger)


if __name__ == '__main__':
    main()
