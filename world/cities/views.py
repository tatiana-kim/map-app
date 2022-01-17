# from django.views.generic import DetailView
# from .models import City

from django.views.generic.base import TemplateView


class CitiesMapView(TemplateView):
    """Cities map view."""

    template_name = "cities/city.html"
