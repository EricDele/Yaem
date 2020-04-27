from django.db import models
from django.conf import settings


class Manager(models.Model):
    """Model class managing the application"""

    # Fields
    key = models.CharField(max_length=64, primary_key=True, null=False)
    value = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        # Default ordering
        ordering = ['key']

    def __str__(self):
        """String for representing"""
        return self.key + " = " + self.value


class Environment(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Datacenter(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DatacenterRoom(models.Model):
    center = models.ForeignKey(Datacenter, null=False, blank=False, on_delete=models.PROTECT)
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.center.__str__() + " : " + self.name

    class Meta:
        unique_together = [['center', 'name']]


class Cluster(models.Model):
    room = models.ForeignKey(DatacenterRoom, null=False, blank=False, on_delete=models.PROTECT)
    name = models.CharField(max_length=64, null=False, blank=False)
    environment = models.ForeignKey(Environment, null=False, blank=False, on_delete=models.PROTECT)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room.__str__() + " : " + self.environment.__str__() + " : " + self.name

    class Meta:
        unique_together = [['room', 'name', 'environment']]


class HostType(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class HostStatus(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Hardware(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    generation = models.CharField(max_length=64, null=True, blank=True)
    cpu_nb = models.IntegerField(null=False, blank=False)
    cpu_speed = models.FloatField(null=False, blank=False)
    cores_nb = models.IntegerField(null=False, blank=False)
    threads_nb = models.IntegerField(null=False, blank=False)
    gpu_speed = models.FloatField(null=False, blank=False)
    gpu_nb = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name


class Host(models.Model):
    hostname = models.CharField(max_length=128, null=False, blank=False, unique=True)
    fqdn_hostname = models.CharField(max_length=128, null=False, blank=False, unique=True)
    services = models.ManyToManyField(Service)
    groups = models.ManyToManyField(Group)
    hardware = models.ForeignKey(Hardware, null=False, blank=False, on_delete=models.PROTECT)
    description = models.TextField(max_length=500, null=True, blank=True)
    cluster = models.ForeignKey(Cluster, null=False, blank=False, on_delete=models.PROTECT)
    host_type = models.ForeignKey(HostType, null=False, blank=False, on_delete=models.PROTECT)
    host_status = models.ForeignKey(HostStatus, null=False, blank=False, on_delete=models.PROTECT)
    rack = models.CharField(max_length=64, null=False)
    rack_position = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hostname

    class Meta:
        unique_together = [['hostname', 'cluster'], ['fqdn_hostname', 'cluster']]


class Disk(models.Model):
    server = models.ForeignKey(Host, null=False, blank=False, on_delete=models.PROTECT)
    disk_type = models.CharField(max_length=50, null=False, blank=False)
    size = models.FloatField(null=False, blank=False)
    interface = models.CharField(max_length=64, null=False, blank=False)
    raid_level = models.IntegerField(null=False, blank=False)
    volume_size = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.server.__str__() + " : " + self.disk_type

    class Meta:
        unique_together = [['server', 'disk_type']]


class Address(models.Model):
    server = models.ForeignKey(Host, null=False, blank=False, on_delete=models.PROTECT)
    address_type = models.CharField(max_length=50, null=False, blank=False)
    ref_address = models.CharField(max_length=64, null=False, blank=False, unique=True)
    mac_address = models.CharField(max_length=64, null=False, blank=False, unique=True)
    interface = models.CharField(max_length=64, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.server.__str__() + " : " + self.address_type + " : " + self.ref_address


class Variable(models.Model):
    key = models.CharField(max_length=64, null=False, blank=False)
    value = models.CharField(max_length=64, null=False, blank=False)
    hostname = models.ForeignKey(Host, null=True, blank=True, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        base = str(self.hostname) if self.hostname is not None else str(self.group)
        return base + " : " + self.key + " : " + self.value
