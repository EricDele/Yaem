from django.shortcuts import render

from rest_framework import viewsets

# Create your views here.
from .serializers import ManagerSerializer
from .serializers import Env_typeSerializer
from .serializers import Host_typeSerializer
from .serializers import Host_statusSerializer
from .serializers import ServiceSerializer
from .serializers import ServerSerializer
from .serializers import ClusterSerializer
from .serializers import GroupSerializer
from .serializers import HostSerializer
from .serializers import VariableSerializer

from .models import Manager
from .models import Env_type
from .models import Host_type
from .models import Host_status
from .models import Service
from .models import Server
from .models import Cluster
from .models import Group
from .models import Host
from .models import Variable



class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all().order_by('key')
    serializer_class = ManagerSerializer

class Env_typeViewSet(viewsets.ModelViewSet):
    queryset = Env_type.objects.all().order_by('name')
    serializer_class = Env_typeSerializer

class Host_typeViewSet(viewsets.ModelViewSet):
    queryset = Host_type.objects.all().order_by('name')
    serializer_class = Host_typeSerializer

class Host_statusViewSet(viewsets.ModelViewSet):
    queryset = Host_status.objects.all().order_by('name')
    serializer_class = Host_statusSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializer

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all().order_by('name')
    serializer_class = ServerSerializer

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
