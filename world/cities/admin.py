from django.contrib.gis import admin

from cities.models import City


@admin.register(City)
class CityAdmin(admin.OSMGeoAdmin):
    """City admin."""

    list_display = ("name", "location")
