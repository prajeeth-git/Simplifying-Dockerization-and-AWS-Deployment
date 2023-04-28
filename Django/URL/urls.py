from django.contrib import admin
from django.urls import path,re_path

from urlshortner.views import urlview,Homeview
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',Homeview.as_view()),
    re_path(r"^(?P<short>[\w-]+)/$", urlview.as_view(),name="scode"),

]
