from rest_framework.routers import SimpleRouter

from .views import PlacesViewSet

# create the endpoint places
route = SimpleRouter()
route.register('places',PlacesViewSet)
