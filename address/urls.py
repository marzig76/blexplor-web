from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<address>[a-zA-Z0-9]+)/$', views.address, name='address'),
]

