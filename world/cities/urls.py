from django.urls import path

from cities.views import CitiesMapView

app_name = "cities"

urlpatterns = [
    path("map/", CitiesMapView.as_view()),
]
