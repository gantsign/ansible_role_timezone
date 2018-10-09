import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_version(host):
    version = host.check_output('date +"%Z"')
    pattern = r'^(BST|GMT)$'
    assert re.search(pattern, version)