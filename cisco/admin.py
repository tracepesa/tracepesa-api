from django.contrib import admin
from cisco.models import CiscoRouter
from cisco.models import CiscoRouterInterface, RouterLink, Vrf
# Register your models here.
admin.site.register(CiscoRouter)
admin.site.register(CiscoRouterInterface)
admin.site.register(Vrf)
admin.site.register(RouterLink)