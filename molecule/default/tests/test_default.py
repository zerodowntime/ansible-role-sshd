import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_running_and_enabled(host):
    distribution = host.system_info.distribution

    if distribution == 'centos':
        serviceName = 'sshd'
    elif distribution == 'ubuntu':
        serviceName = 'ssh'

    service = host.service(serviceName)

    assert service.is_running
    assert service.is_enabled
