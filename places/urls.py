from django.contrib import admin
from django.urls import path, include

from core.urls import route


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(route.urls)),
]
