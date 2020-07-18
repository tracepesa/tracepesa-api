from ciscoconfparse import CiscoConfParse

# from cisco.api.service import router_get_or_create
import cisco.api.service as service
from ipaddress import IPv4Interface


def parse_config_file(file):
    cfg = CiscoConfParse(file)
    router = service.router_get_or_create(get_hostname(cfg))
    interfaces = get_interfaces(cfg)
    service.interfaces_update_or_create(interfaces, router)


def get_hostname(cfg):
    hostname_obj = cfg.find_objects(r'^hostname')[0]
    return hostname_obj.re_match_typed(r'^hostname\s+(\S+)', default='')


def get_interfaces(cfg):
    # Get interfaces
    intfs_cfg = []  # make sure we start with an empty list

    # extract interfaces that do not have a vrf definition
    for obj in cfg.find_objects_wo_child(parentspec=r"^interf", childspec=r"vrf"):
        int_name = obj.text.split()[1]
        # extract ipv4 address
        for ip4 in obj.re_search_children(r'^\s+ipv4\s+address'):
            ip_intf = {'name': int_name}
            ip_intf['ipv4_address'] = int_ipv4 = ip4.re_match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', group=0)
            ip_intf['ipv4_mask'] = int_ipv4mask = ip4.re_match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s(\S+)', group=1)
            ip_intf['ipv4_network'] = str(IPv4Interface(int_ipv4 + '/' + int_ipv4mask).network)
            intfs_cfg.append(ip_intf)

    return intfs_cfg
