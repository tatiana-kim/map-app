"""Cities API URL Configuration."""

from rest_framework import routers

from cities.viewsets import CitiesViewSet

router = routers.DefaultRouter()
router.register(r"cities", CitiesViewSet)

urlpatterns = router.urls
