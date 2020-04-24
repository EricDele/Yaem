from rest_framework import serializers

from .models import Manager
from .models import Environment
from .models import HostType
from .models import HostStatus
from .models import Service
from .models import Cluster
from .models import Group
from .models import Host
from .models import Variable
from .models import Datacenter
from .models import DatacenterRoom
from .models import Disk
from .models import Address


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('key', 'value')


class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Environment
        fields = ('name',)


class HostTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HostType
        fields = ('name',)


class HostStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HostStatus
        fields = ('name',)


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('name',)


class ClusterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cluster
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'


class VariableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variable
        fields = '__all__'
