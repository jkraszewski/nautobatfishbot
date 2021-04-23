import netmiko
from getpass import getpass
import yaml
from pprint import pprint


def open_yml_file(yml_file):
    with open(yml_file) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        yml_data = yaml.load(file, Loader=yaml.FullLoader)
    return yml_data


def make_connection(ip, username, password):
    net_connect = netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)
    return net_connect


def send_command(net_connect, command):
    return net_connect.send_command_expect(command)


username = 'ntc'
password = getpass()
yml_file = 'build_data.yml'
router_data = open_yml_file(yml_file)


for router in router_data:
    net_connect = make_connection(router['name'], username, password)
    for interface in router['interfaces']:
        for interface_name, ip_snm in interface.items():
            config = [
                f'interface {interface_name}',
                f'ip address {ip_snm}',
                'no shut',
                'cdp enable'
            ]
            # pprint(config)
            net_connect.send_config_set(config)
    config = [
        'router eigrp 10',
        'network 192.168.0.0 0.0.255.255'
    ]
    net_connect.send_config_set(config)
