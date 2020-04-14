from django.db import models

# Create your models here.

class Manager(models.Model):
    """Model class managing the application"""

    # Fields
    key = models.CharField(max_length=64, primary_key=True, null=False)
    value = models.CharField(max_length=256, null=False)

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['key']

    def __str__(self):
        """String for representing"""
        return self.key + " = " + self.value

class Env_type(models.Model):
    """Model class for defining environment types"""

    # Fields
    name = models.CharField(max_length=64, null=False)

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['name']

    def __str__(self):
        """String for representing"""
        return self.name

class Host_type(models.Model):
    """Model class for defining host types"""

    # Fields
    name = models.CharField(max_length=64, null=False)

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['name']

    def __str__(self):
        """String for representing"""
        return self.name

class Host_status(models.Model):
    """Model class for defining host status"""

    # Fields
    name = models.CharField(max_length=64, null=False)

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['name']

    def __str__(self):
        """String for representing"""
        return self.name

class Service(models.Model):
    """Model class for defining a service"""

    # Fields
    name = models.CharField(max_length=64, null=False)

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['name']

    def __str__(self):
        """String for representing"""
        return self.name

class Server(models.Model):
    """Model class for defining a server"""

    # Fields
    name = models.CharField(max_length=64, null=False)
    cpu = models.CharField(max_length=64, null=False)
    memory = models.PositiveIntegerField()
    u_size = models.PositiveSmallIntegerField(default=1)
    end_support = models.DateField()

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['name']

    def __str__(self):
        """String for representing"""
        return self.name

class Cluster(models.Model):
    """Model class for defining a cluster"""

    # Fields
    name = models.CharField(max_length=64, null=False)
    env = models.ForeignKey(Env_type, on_delete=models.CASCADE)

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['name']

    def __str__(self):
        """String for representing"""
        return self.name

class Group(models.Model):
    """Model class for defining groups"""

    # Fields
    name = models.CharField(max_length=64, null=False)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['name']

    def __str__(self):
        """String for representing"""
        return self.name

class Host(models.Model):
    """Model class for defining a host"""

    # Fields
    hostname = models.CharField(max_length=128, null=False)
    fqdn_hostname = models.CharField(max_length=128, null=False)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    host_type = models.ForeignKey(Host_type, on_delete=models.CASCADE)
    host_status = models.ForeignKey(Host_status, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    service = models.ManyToManyField(Service)
    rack = models.CharField(max_length=64, null=False)
    rack_position = models.PositiveSmallIntegerField()

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['hostname']

    def __str__(self):
        """String for representing"""
        return self.hostname

class Variable(models.Model):
    """Model class managing variables"""

    # Fields
    key = models.CharField(max_length=64, null=False)
    value = models.CharField(max_length=256, null=False)
    hostname = models.ForeignKey(Host, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['key']

    def __str__(self):
        """String for representing"""
        return self.key + " = " + self.value
