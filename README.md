# ansible-dependencies

Inspired / Cloned from [portable-ansible](https://github.com/ownport/portable-ansible)

## pip meta package

Install dependencies for docker, ipaddr, vault, rabbit, nsupdate, nxos, scp
```bash
pip install ansible-dependencies
```
Install dependencies for aws, vmware, OpenStack, CloudStack, OpenShift, Heroku
```bash
pip install ansible-dependencies[cloud]
```
Install dependencies for F5, Palo Alto, Infoblox, EMC, netconf, Juniper
```bash
pip install ansible-dependencies[network]
```
Install dependencies for testing ansible
```bash
pip install ansible-dependencies[test]
```
Install everything
```bash
pip install ansible-dependencies[all]
```

## Standalone Packages

Standalone packages with bundled dependencies - Only requires python to run and is unaffected by global python/pip paths.


### RPM
```bash
# python 2
rpm -i https://github.com/moshloop/ansible-dependencies/releases/download/2.6.5.1/portable-ansible-py2-2.6.5-1.x86_64.rpm
# python 3
rpm -i https://github.com/moshloop/ansible-dependencies/releases/download/2.6.5.1/portable-ansible-py3-2.6.5-1.x86_64.rpm
ansible --version
```

```ansible 2.6.5
  config file = None
  configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/ansible/ansible/ansible
  executable location = /usr/local/ansible/ansible
  python version = 3.7.0 (default, Sep  5 2018, 03:25:31) [GCC 6.3.0 20170516]
```

### DEB
```bash
# python 2
wget https://github.com/moshloop/ansible-dependencies/releases/download/2.6.5.1/portable-ansible-py2_2.6.5_amd64.deb
# python 3
wget https://github.com/moshloop/ansible-dependencies/releases/download/2.6.5.1/portable-ansible-py3_2.6.5_amd64.deb
dpkg -i portable-ansible-py3_2.6.5_amd64.deb
```