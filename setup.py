
from subprocess import *
from setuptools import setup, find_packages
import os

minimal = [
    'docker-py',
    'certifi',
    'cryptography',
    'dnspython',
    'ipaddress',
    'jmespath',
    'netaddr',
    'passlib',
    'pexpect',
    'pyOpenSSL==16.2.0',
    #    'python-ldap', requires source compilation
    'requests',
    'requests_ntlm',
    'scp',
    'urllib3==1.22'
    ]
test = [
    'pycodestyle',
    'pylint',
    'pytest',
    'virtualenv',
    'yamllint',
    'mock',
    'junit_xml'
    ]

cloud = [
    'apache-libcloud',
    'aws-sudo',
    'awscli',
    'boto',
    'cidrtrie',
    'cs',
    'f5-sdk',
    'github3.py',
    'heroku3',
    'infoblox-client',
    'jxmlease',
    'ncclient',
    'openshift',
    'pandevice',
    'pyvmomi',
    'pywinrm[credssp]',
    'pywinrm[kerberos]',
    's3cmd',
    'storops',
    'textfsm',
    'vapi-client-bindings',
    'zabbix-api'
]

setup(
    name = 'ansible-dependencies', version = '2.6.5',
    url = 'https://www.github.com/moshloop/ansible-dependencies',
    install_requires= minimal,
    extras_require = dict(
        cloud=cloud,
        all=cloud + test,
        test=test),
    author = 'Moshe Immerman', author_email = 'firstname.surname@gmail.com'
    )