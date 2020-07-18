from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cisco.models import RouterLink
from cisco.api.serializers import CiscoRouterSerializers, RouterLinkSerializers
from cisco.models import CiscoRouter
from cisco.api.tasks import parse_config_background


@api_view(['GET'])
def parse_config(request):
    parse_config_background('files/')
    return Response(status=status.HTTP_200_OK)


class RouterLinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RouterLink.objects.all()
    serializer_class = RouterLinkSerializers


class CiscoRouterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CiscoRouter.objects.all()
    serializer_class = CiscoRouterSerializers
