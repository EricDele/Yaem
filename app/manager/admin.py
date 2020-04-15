from django.contrib import admin

# Register your models here.
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

admin.site.register(Manager)
admin.site.register(EnvType)
admin.site.register(HostType)
admin.site.register(HostStatus)
admin.site.register(Service)
admin.site.register(Server)
admin.site.register(Cluster)
admin.site.register(Group)
admin.site.register(Host)
admin.site.register(Variable)
