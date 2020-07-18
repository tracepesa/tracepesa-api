import os
from cisco.api.confparse import parse_config_file
from cisco.models import CiscoRouter, CiscoRouterInterface, RouterLink
from django.db import transaction


def parse_config_from_dir(dir):
    files = os.listdir(dir)

    for f in files:
        parse_config_file(open(dir + f))


def parse_config_from_ftp():
    pass


def parse_config_from_file(file):
    pass


def router_get_or_create(hostname):
    router, created = CiscoRouter.objects.get_or_create(name=hostname)
    if created:
        print('New router created:' + hostname)
    return router


def interfaces_update_or_create(interfaces, router):
    with transaction.atomic():
        for intf in interfaces:
            CiscoRouterInterface.objects.update_or_create(name=intf['name'], ipv4_address=intf['ipv4_address'],
                                                          ipv4_mask=intf['ipv4_mask'],
                                                          ipv4_network=intf['ipv4_network'], router=router)


def links_update_or_create():
    interfaces = CiscoRouterInterface.objects.all()

    for interface in interfaces:
        match_interface = interfaces.filter(ipv4_network=interface.ipv4_network).exclude(ipv4_address=interface.ipv4_address).first()
        existing_links = RouterLink.objects.filter(source=interface, target=match_interface) | RouterLink.objects.filter(source=match_interface, target=interface)
        if match_interface and existing_links.count() == 0:
            RouterLink(source=interface, target=match_interface).save()
