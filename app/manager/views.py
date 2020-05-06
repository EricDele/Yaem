from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication

# Create your views here.
from .serializers import ManagerSerializer
from .serializers import EnvironmentSerializer
from .serializers import HostTypeSerializer
from .serializers import HostStatusSerializer
from .serializers import ServiceSerializer
from .serializers import ClusterSerializer
from .serializers import GroupSerializer
from .serializers import HostSerializer
from .serializers import VariableSerializer
from .serializers import DatacenterSerializer
from .serializers import DatacenterRoomSerializer
from .serializers import DiskSerializer
from .serializers import AddressSerializer
from .serializers import HardwareSerializer

from .models import Manager
from .models import Environment
from .models import Datacenter
from .models import DatacenterRoom
from .models import HostType
from .models import HostStatus
from .models import Service
from .models import Cluster
from .models import Group
from .models import Host
from .models import Disk
from .models import Address
from .models import Variable
from .models import Hardware


class ManagerViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Manager.objects.all().order_by('key')
    serializer_class = ManagerSerializer


class EnvironmentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Environment.objects.all().order_by('name')
    serializer_class = EnvironmentSerializer


class DatacenterViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Datacenter.objects.all().order_by('name')
    serializer_class = DatacenterSerializer


class DatacenterRoomViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = DatacenterRoom.objects.all().order_by('name')
    serializer_class = DatacenterRoomSerializer


class HostTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = HostType.objects.all().order_by('name')
    serializer_class = HostTypeSerializer


class HostStatusViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = HostStatus.objects.all().order_by('name')
    serializer_class = HostStatusSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializer


class ClusterViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Cluster.objects.all().order_by('name')
    serializer_class = ClusterSerializer


class GroupViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer


class HostViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Host.objects.all().order_by('hostname')
    serializer_class = HostSerializer


class VariableViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Variable.objects.all().order_by('key')
    serializer_class = VariableSerializer


class DiskViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Disk.objects.all().order_by('disk_type')
    serializer_class = DiskSerializer


class AddressViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all().order_by('address_type')
    serializer_class = AddressSerializer


class HardwareViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Hardware.objects.all().order_by('name')
    serializer_class = HardwareSerializer

