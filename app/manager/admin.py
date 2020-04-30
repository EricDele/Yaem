from django.contrib import admin

# Register your models here.
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
from .models import Hardware

admin.site.register(Manager)
admin.site.register(Environment)
admin.site.register(HostType)
admin.site.register(HostStatus)
admin.site.register(Service)
admin.site.register(Cluster)
admin.site.register(Group)
admin.site.register(Host)
admin.site.register(Variable)
admin.site.register(Datacenter)
admin.site.register(DatacenterRoom)
admin.site.register(Disk)
admin.site.register(Address)
admin.site.register(Hardware)
