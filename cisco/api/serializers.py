from rest_framework import serializers
from cisco.models import CiscoRouter, RouterLink, CiscoRouterInterface


class RouterSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiscoRouter
        fields = ['name']


class SourceSerializer(serializers.ModelSerializer):
    router = RouterSourceSerializer()

    class Meta:
        model = CiscoRouterInterface
        fields = ['router']


class RouterLinkSerializers(serializers.ModelSerializer):
    source = SourceSerializer()
    target = SourceSerializer()

    class Meta:
        model = RouterLink
        fields = ['source', 'target']


class CiscoRouterInterfaceSerializers(serializers.ModelSerializer):
    source = RouterLinkSerializers(many=True, read_only=True)
    target = RouterLinkSerializers(many=True, read_only=True)

    class Meta:
        model = CiscoRouterInterface
        fields = ['id', 'name', 'ipv4_address', 'ipv4_mask', 'ipv4_network', 'vlan', 'vrf', 'source', 'target']


class CiscoRouterSerializers(serializers.ModelSerializer):
    interfaces = CiscoRouterInterfaceSerializers(many=True, read_only=True)

    class Meta:
        model = CiscoRouter
        fields = ['id', 'name', 'interfaces']
