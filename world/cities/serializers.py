"""Cities serializers."""

from rest_framework_gis import serializers

from .models import City


class CitiesSerializer(serializers.GeoFeatureModelSerializer):
    """Cities GeoJSON serializer."""

    class Meta:
        """Cities serializer meta class."""

        fields = ("id", "name")
        geo_field = "location"
        model = City
