from pyexpat import model
from rest_framework import serializers
from .models import Places


class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = (
            'id',
            'name',
            'slug',
            'city',
            'state',
            'created_at',
            'update_at'
        )