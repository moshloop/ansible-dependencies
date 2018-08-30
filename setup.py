
from subprocess import *
from setuptools import setup, find_packages
import os

setup(
    name = 'ansible-dependencies', version = '2.6.1',
    install_requires=[
    'yq',
    'urllib3==1.22',
    'jmespath',
    'certifi',
    'netaddr',
    'awscli',
    'aws-sudo',
    's3cmd',
    'boto',
    'pandevice',
    'f5-sdk',
    'dnspython',
    'cidrtrie',
    'textfsm',
    'pandas',
    'openpyxl',
    'pywinrm[kerberos]',
    'pywinrm[credssp]',
    'requests',
    'requests_ntlm',
    'cryptography',
    'pyvmomi',
    'apache-libcloud',
    'vapi-client-bindings',
    'pyOpenSSL==16.2.0',
    ],
    url = 'https://www/github.com/moshloop/ansible-dependencies',
    author = 'Moshe Immerman', author_email = 'firstname.surname@gmail.com'
    )