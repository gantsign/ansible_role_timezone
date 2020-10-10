import re


def test_version(host):
    version = host.check_output('date +"%Z"')
    pattern = r'^(BST|GMT)$'
    assert re.search(pattern, version)
