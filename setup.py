
from subprocess import *
from setuptools import setup, find_packages
import os

minimal = [
    'docker',
    'docker-compose',
    'wheel',
    'certifi',
    'cryptography',
    'dnspython',
    'ipaddress',
    'jmespath',
    'cidrtrie',
    'netaddr',
    'hvac', # Hashicorp Vault lookup
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
    'pylint==1.9.3',
    'pytest',
    'ansible-lint',
    'virtualenv',
    'voluptuous',
    'yamllint',
    'mock',
    'junit_xml'
    ]

network = [
    'bigsuds',
    'deepdiff',
    'f5-sdk', # F5 Load balancers,
    'infoblox-client',
    'jxmlease',
    'ncclient', # netconf
    'objectpath',
    'pandevice', # Palo Alto Firewall,
    'storops', # EMC
    'textfsm',
]

cloud = [
    'apache-libcloud',
    'aws-sudo',
    'awscli',
    'boto',
    'boto3',
    'cs', #cloudstack
    'github3.py',
    'heroku3',
    'openshift',
    'pyrax', #OpenStack
    'pyvmomi', #VMWare
    'pywinrm[credssp]',
    'pywinrm[kerberos]',
    's3cmd',
    'vapi-client-bindings'
]

setup(
    name = 'ansible-dependencies', version = '2.7',
    url = 'https://www.github.com/moshloop/ansible-dependencies',
    install_requires= minimal,
    extras_require = dict(
        cloud=cloud,
        network=network,
        all=cloud + test + network,
        test=test),
    author = 'Moshe Immerman', author_email = 'firstname.surname@gmail.com'
    )