"""geometry API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from .models import City
from cities.serializers import CitiesSerializer


class CitiesViewSet(viewsets.ReadOnlyModelViewSet):
    """ City view set """
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = City.objects.all()
    serializer_class = CitiesSerializer
