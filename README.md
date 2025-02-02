waco_bootstrap_test
===================

![test](https://github.com/waco-org/waco-bootstrap-test/actions/workflows/test.yml/badge.svg)

This Ansible role serves the sole purpose of testing the ``waco-bootstrap`` project on different
platforms. At this time tests are run on Rocky Linux 9, CentOS Stream 10, CentOS Stream 9,
Fedora 41, Fedora 40, Fedora 39, Ubuntu 24.04 and Ubuntu 22.04.


Requirements
------------

None.

Role Variables
--------------

None.

Dependencies
------------

See the ``waco-bootstrap`` project.

Example Playbook
----------------

While it is certainly possible to use this role by itself, it is meant to be used in conjunction
with the [waco-master](https://github.com/waco-org/waco-master) role.

    - hosts: servers
      roles:
         - role: waco_org.waco_bootstrap_test

License
-------

GPLv3

Author Information
------------------

Nicola Musatti - <https://github.com/nmusatti>

WACO - Workstation as Code - <https://github.com/waco-org>
