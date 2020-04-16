from rest_framework import serializers

from .models import Manager
from .models import EnvType
from .models import HostType
from .models import HostStatus
from .models import Service
from .models import Server
from .models import Cluster
from .models import Group
from .models import Host
from .models import Variable


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('key', 'value')


class EnvTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnvType
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


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'


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
