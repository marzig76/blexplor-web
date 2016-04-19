from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<search_string>[a-zA-Z0-9]+)/$', views.search_string, name='search_string'),
]
