from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'manager', views.ManagerViewSet)
router.register(r'environment', views.EnvironmentViewSet)
router.register(r'datacenter', views.DatacenterViewSet)
router.register(r'datacenter_room', views.DatacenterRoomViewSet)
router.register(r'cluster', views.ClusterViewSet)
router.register(r'host_type', views.HostTypeViewSet)
router.register(r'host_status', views.HostStatusViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'hardware', views.HardwareViewSet)
router.register(r'host', views.HostViewSet)
router.register(r'disk', views.DiskViewSet)
router.register(r'address', views.AddressViewSet)
router.register(r'variable', views.VariableViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]