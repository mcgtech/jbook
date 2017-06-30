from django.conf.urls import url
from . import views
from booking.views import *

urlpatterns = [
    url(r'^booking/new/$', views.booking_new, name='booking_new'),
    url(r'^booking/(?P<pk>\d+)/edit/$', views.booking_edit, name='booking_edit'),
    url(r'^booking_search/$', BookingViewFilter.as_view(), name='booking_search'),
    url(r'^booking_calendar/(?P<prop_id>\d+)/(?P<pYear>\d+)/(?P<pMonth>\d+)/$', views.booking_calendar, name='booking_calendar'),
]