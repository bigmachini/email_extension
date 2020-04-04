============================
email-extension
============================

email-extension is a python package  that is going to simplify sending emails from a python application

This module is for Python 3.6 and above!

INSTALLATION
============================

prerequisits:

https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/#persistent-environment-variables

create an environment variable with the name EE_CONFIG

this can be done by:

    sudo nano /etc/enviroment

add the following line and save:

    EE_CONFIG="PATH_TO_CONFIG_FOLDER"

update your current shell by: NOTE: Restart is needed for effect to take place globally

    source /etc/enviroment

Create a settings file within the directory. by default the system will look for settings.ini
if the name was changed you will have to pass the new file name to get_config when getting the
config

    cd PATH_TO_CONFIG_FOLDER

copy SampleSettingsFile_ into settings.ini and update with appropriate smtp details

    nano settings.ini

You can install the package with pip:

    pip install email-extension


USAGE
============================

Importing helper:

    from email_extension import email_helper

Get config and logger from settings.ini in the EE_CONFIG folder
    config,logger = email_helper.get_config()

if you changed the config file name from settings.ini you will have to pass the name of the config file
    config,logger = email_helper.get_config(filename)


:code:`check_regex` will check will the email address has a valid structure and defaults to True

:code:`check_mx`: check the mx-records and check whether the email actually exists

:code:`from_address`: the email address the probe will be sent from,

:code:`helo_host`: the host to use in SMTP HELO when checking for an email,

:code:`smtp_timeout`: seconds until SMTP timeout

:code:`dns_timeout`: seconds until DNS timeout

:code:`use_blacklist`: use the blacklist of domains downloaded from https://github.com/martenson/disposable-email-domains

Auto-updater
============================



TODOs and BUGS
============================
See: https://github.com/bigmachini/email_extension/issues




More Resources
============================

-   [What is setup.py?] on Stack Overflow
-   [Official Python Packaging User Guide](https://packaging.python.org)
-   [The Hitchhiker's Guide to Packaging]
-   [Cookiecutter template for a Python package]

License
============================
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any means.
.. _SampleSettingsFile: http://www.python.org/
  [an example setup.py]: https://github.com/navdeep-G/setup.py/blob/master/setup.py
  [PyPi]: https://docs.python.org/3/distutils/packageindex.html
  [Twine]: https://pypi.python.org/pypi/twine
  [image]: https://farm1.staticflickr.com/628/33173824932_58add34581_k_d.jpg
  [What is setup.py?]: https://stackoverflow.com/questions/1471994/what-is-setup-py
  [The Hitchhiker's Guide to Packaging]: https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html
  [Cookiecutter template for a Python package]: https://github.com/audreyr/cookiecutter-pypackage