from django.contrib import admin
from .models import Places


@admin.register(Places)
class PlaceAdmin(admin.ModelAdmin):
    pass