README.md
=======================
prerequisits:

https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/#persistent-environment-variables


create an enviroment variable with the name EE_CONFIG

this can be done by:

sudo nano  /etc/enviroment

add the following line and save:

export EE_CONFIG = 'PATH_TO_CONFIG_FOLDER'

source /etc/enviroment

cd PATH_TO_CONFIG_FOLDER

copy the settings_sample.ini into settings.ini and filling in the appropriate smtp details
nano settings.ini
 
Installation


To Do
-----



More Resources
--------------

-   [What is setup.py?] on Stack Overflow
-   [Official Python Packaging User Guide](https://packaging.python.org)
-   [The Hitchhiker's Guide to Packaging]
-   [Cookiecutter template for a Python package]

License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any means.

  [an example setup.py]: https://github.com/navdeep-G/setup.py/blob/master/setup.py
  [PyPi]: https://docs.python.org/3/distutils/packageindex.html
  [Twine]: https://pypi.python.org/pypi/twine
  [image]: https://farm1.staticflickr.com/628/33173824932_58add34581_k_d.jpg
  [What is setup.py?]: https://stackoverflow.com/questions/1471994/what-is-setup-py
  [The Hitchhiker's Guide to Packaging]: https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html
  [Cookiecutter template for a Python package]: https://github.com/audreyr/cookiecutter-pypackage