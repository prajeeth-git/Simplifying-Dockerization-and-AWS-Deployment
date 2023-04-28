from django.urls import path,re_path
from .views import wildcard_redirect
from django.contrib import admin

urlpatterns = [
    path('^(?P<path>.*)', admin.site.urls),
]
