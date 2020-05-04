from django.shortcuts import render

from rest_framework import viewsets

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
    queryset = Manager.objects.all().order_by('key')
    serializer_class = ManagerSerializer


class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all().order_by('name')
    serializer_class = EnvironmentSerializer


class DatacenterViewSet(viewsets.ModelViewSet):
    queryset = Datacenter.objects.all().order_by('name')
    serializer_class = DatacenterSerializer


class DatacenterRoomViewSet(viewsets.ModelViewSet):
    queryset = DatacenterRoom.objects.all().order_by('name')
    serializer_class = DatacenterRoomSerializer


class HostTypeViewSet(viewsets.ModelViewSet):
    queryset = HostType.objects.all().order_by('name')
    serializer_class = HostTypeSerializer


class HostStatusViewSet(viewsets.ModelViewSet):
    queryset = HostStatus.objects.all().order_by('name')
    serializer_class = HostStatusSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializer


class ClusterViewSet(viewsets.ModelViewSet):
    queryset = Cluster.objects.all().order_by('name')
    serializer_class = ClusterSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all().order_by('hostname')
    serializer_class = HostSerializer


class VariableViewSet(viewsets.ModelViewSet):
    queryset = Variable.objects.all().order_by('key')
    serializer_class = VariableSerializer


class DiskViewSet(viewsets.ModelViewSet):
    queryset = Disk.objects.all().order_by('disk_type')
    serializer_class = DiskSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('address_type')
    serializer_class = AddressSerializer


class HardwareViewSet(viewsets.ModelViewSet):
    queryset = Hardware.objects.all().order_by('name')
    serializer_class = HardwareSerializer

