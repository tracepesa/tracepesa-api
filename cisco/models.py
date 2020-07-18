from django.db import models


# Create your models here.

class CiscoRouter(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Vrf(models.Model):
    name = models.CharField(max_length=100)
    rt = models.CharField(max_length=20)
    router = models.ForeignKey(CiscoRouter, null=True, blank=True, related_name='vrfs', on_delete=models.CASCADE)


class CiscoRouterInterface(models.Model):
    name = models.CharField(max_length=100)
    ipv4_address = models.CharField(max_length=100, null=True, blank=True)
    ipv4_mask = models.CharField(max_length=100, null=True, blank=True)
    ipv4_network = models.CharField(max_length=100, null=True, blank=True)
    vlan = models.CharField(max_length=10, null=True, blank=True)
    vrf = models.ForeignKey(Vrf, on_delete=models.CASCADE, null=True, blank=True)
    router = models.ForeignKey(CiscoRouter, related_name='interfaces', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'router')


class RouterLink(models.Model):
    source = models.ForeignKey(CiscoRouterInterface, related_name='source', on_delete=models.CASCADE)
    target = models.ForeignKey(CiscoRouterInterface, related_name='target', on_delete=models.CASCADE)
