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

    pip install -i https://test.pypi.org/simple/ email-extension


USAGE
============================

Importing helper:

    from email_extension import email_helper

Get config and logger from settings.ini in the EE_CONFIG folder
    config,logger = email_helper.get_config()

if you changed the config file name from settings.ini you will have to pass the name of the config file
    config,logger = email_helper.get_config(filename)

Get the email helper object that will be used to send the email
 eh = email_helper.get_email_helper(config, logger)

call the send email command when sending and email _to,_subject,_body are mandatory other parameters are optional
 eh.email(_to, _subject, _body)


TODOs and BUGS
============================
See: https://github.com/bigmachini/email_extension/issues


More Resources
============================


License
============================
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any means.

.. _SampleSettingsFile: https://raw.githubusercontent.com/bigmachini/email_extension/master/email_extension/config/settings_sample.ini