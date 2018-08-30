
from subprocess import *
from setuptools import setup, find_packages
import os

setup(
    name = 'ansible-dependencies', version = '2.6.1.4',
    install_requires=[
    'apache-libcloud',
    'aws-sudo',
    'awscli',
    'boto',
    'certifi',
    'cidrtrie',
    'cryptography',
    'cs',
    'dnspython',
    'docker-compose',
    'docker-py',
    'f5-sdk',
    'github3.py',
    'heroku3',
    'infoblox-client',
    'ipaddress',
    'jmespath',
    'junit_xml',
    'jxmlease',
    'mock',
    'ncclient',
    'netaddr',
    'openpyxl',
    'openshift',
    'pandas',
    'pandevice',
    'passlib',
    'pexpect',
    'pycodestyle',
    'pylint',
    'pyOpenSSL==16.2.0',
    'pytest',
#    'python-ldap', requires source compilation
    'pyvmomi',
    'pywinrm[credssp]',
    'pywinrm[kerberos]',
    'requests',
    'requests_ntlm',
    's3cmd',
    'scp',
    'storops',
    'textfsm',
    'urllib3==1.22',
    'vapi-client-bindings',
    'yamllint',
    'yq',
    'zabbix-api'
    ],
    url = 'https://www/github.com/moshloop/ansible-dependencies',
    author = 'Moshe Immerman', author_email = 'firstname.surname@gmail.com'
    )