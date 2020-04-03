import os
import pathlib
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="email-extension",
    version="1.5.0",
    description="This is a package to make the sending of emails in python easy",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bigmachini/email_extension",
    author="Bigmachini.Inc",
    author_email="info@bigmachini.net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["email_extension"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "emailext=email_extension.__main__:main",
        ]
    },
)