# from django.db import models
from django.contrib.gis.db import models


class City(models.Model):
    """A city with name and location."""

    name = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        """Return string representation."""
        return self.name
    
    class Meta:
        # order of drop-down list items
        # ordering = ('name',)

        # plural form in admin view
        verbose_name_plural = 'cities'
