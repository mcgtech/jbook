from django.conf.urls import url
from . import views
from property.views import *

urlpatterns = [
    url(r'^property/new/$', views.property_new, name='property_new'),
    url(r'^property/(?P<pk>\d+)/edit/$', views.property_edit, name='property_edit'),
    url(r'^property_search/$', views.property_search, name='property_search'),
]