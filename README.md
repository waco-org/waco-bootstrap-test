waco_bootstrap_test
===================

![test](https://github.com/waco-org/waco-bootstrap-test/actions/workflows/test.yml/badge.svg)

This Ansible role serves the sole purpose of testing the
[waco-bootstrap](https://github.com/waco-org/waco-bootstrap.git) project on different
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

See the [waco-bootstrap](https://github.com/waco-org/waco-bootstrap.git) project.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: waco_org.waco_bootstrap_test

Note that this role is not really meant to be run directly from a playbook. In order to run the tests
you need Docker and a recent version of Python with the ``tox`` package installed. Then you might run

    tox run -- test

to run the tests on all the supported platforms, or

    tox run -e rockylinux9 -- test

to run the tests on a specific platform.
    
License
-------

GPLv3

Author Information
------------------

Nicola Musatti - <https://github.com/nmusatti>

WACO - Workstation as Code - <https://github.com/waco-org>
