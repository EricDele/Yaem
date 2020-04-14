from django.contrib import admin

# Register your models here.
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

admin.site.register(Manager)
admin.site.register(Env_type)
admin.site.register(Host_type)
admin.site.register(Host_status)
admin.site.register(Service)
admin.site.register(Server)
admin.site.register(Cluster)
admin.site.register(Group)
admin.site.register(Host)
admin.site.register(Variable)