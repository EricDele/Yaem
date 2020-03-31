from django.db import models

# Create your models here.

class manager(models.Model):
    """Model class managing the application"""

    # Fields
    key = models.CharField(max_length=64, primary_key=True, null=False)
    value = models.CharField(max_length=256, null=False)

    # Metadata
    class Meta: 
        # Default ordering
        ordering = ['key']

    def _str__(self):
        """String for representing"""
        return self.key + " = " + self.value
