from rest_framework import serializers

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


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'


class DatacenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datacenter
        fields = '__all__'


class DatacenterRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DatacenterRoom
        fields = '__all__'


class ClusterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cluster
        fields = '__all__'


class HostTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HostType
        fields = '__all__'


class HostStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HostStatus
        fields = '__all__'


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class HardwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hardware
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'


class DiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disk
        fields = '__all__'


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class VariableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variable
        fields = '__all__'
