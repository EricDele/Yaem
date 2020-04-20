from django.shortcuts import render

from rest_framework import viewsets
#
# # Create your views here.
# from .serializers import ManagerSerializer
# from .serializers import EnvTypeSerializer
# from .serializers import HostTypeSerializer
# from .serializers import HostStatusSerializer
# from .serializers import ServiceSerializer
# from .serializers import ServerSerializer
# from .serializers import ClusterSerializer
# from .serializers import GroupSerializer
# from .serializers import HostSerializer
# from .serializers import VariableSerializer
#
# from .models import Manager
# from .models import EnvType
# from .models import HostType
# from .models import HostStatus
# from .models import Service
# from .models import Server
# from .models import Cluster
# from .models import Group
# from .models import Host
# from .models import Variable
#
#
# class ManagerViewSet(viewsets.ModelViewSet):
#     queryset = Manager.objects.all().order_by('key')
#     serializer_class = ManagerSerializer
#
#
# class EnvTypeViewSet(viewsets.ModelViewSet):
#     queryset = EnvType.objects.all().order_by('name')
#     serializer_class = EnvTypeSerializer
#
#
# class HostTypeViewSet(viewsets.ModelViewSet):
#     queryset = HostType.objects.all().order_by('name')
#     serializer_class = HostTypeSerializer
#
#
# class HostStatusViewSet(viewsets.ModelViewSet):
#     queryset = HostStatus.objects.all().order_by('name')
#     serializer_class = HostStatusSerializer
#
#
# class ServiceViewSet(viewsets.ModelViewSet):
#     queryset = Service.objects.all().order_by('name')
#     serializer_class = ServiceSerializer
#
#
# class ServerViewSet(viewsets.ModelViewSet):
#     queryset = Server.objects.all().order_by('name')
#     serializer_class = ServerSerializer
#
#
# class ClusterViewSet(viewsets.ModelViewSet):
#     queryset = Cluster.objects.all().order_by('name')
#     serializer_class = ClusterSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#
#
# class HostViewSet(viewsets.ModelViewSet):
#     queryset = Host.objects.all().order_by('hostname')
#     serializer_class = HostSerializer
#
#
# class VariableViewSet(viewsets.ModelViewSet):
#     queryset = Variable.objects.all().order_by('key')
#     serializer_class = VariableSerializer
