
from rest_framework import routers
from cisco.api import views
from django.urls import path, include
from cisco.api.views import parse_config

router = routers.DefaultRouter()
router.register(r'router-links', views.RouterLinkViewSet)
router.register(r'routers', views.CiscoRouterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('parse-config', parse_config, name='parse-config')
]
