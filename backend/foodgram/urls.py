"""foodgram URL Configuration"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('recipes.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls.authtoken')),
]
