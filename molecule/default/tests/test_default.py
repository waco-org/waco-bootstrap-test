import os, pathlib

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_waco_user(host):
    assert host.group("waco").exists
    assert host.user("waco").exists
    h = pathlib.Path(host.user("waco").home)
    f = host.file(str(h / ".ssh/authorized_keys"))
    assert f.exists
    assert f.mode == 0o600

def test_waco_installation(host):
    h = pathlib.Path(host.user("waco").home)
    f = host.file(str(h / "waco/settings/master.yml"))
    assert f.exists