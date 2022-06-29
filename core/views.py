from rest_framework import viewsets
from .serializers import PlacesSerializer
from .models import Places


class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
