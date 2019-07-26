from django.urls import re_path
from django.contrib.auth import views as auth_views
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = [
    re_path(r'^driver/trip/$', views.DriverTripListView.as_view(), name = 'driver-trip'),
    re_path(r'^driver/trip/create/$', views.DriverTripCreateView.as_view(), name = 'driver-trip'),
    re_path(r'^driver/trip/active/$', views.DriverActiveTrip.as_view(), name = 'driver-trip-active'),
    re_path(r'^driver/trip/active/abort/(?P<pk>\d+)$', views.DriverAbortActiveTrip.as_view(), name = 'driver-abort-trip-active'),
    re_path(r'^driver/trip/active/end/(?P<pk>\d+)$', views.DriverEndActiveTrip.as_view(), name = 'driver-end-trip-active'),
    re_path(r'^driver/trip/previous/$', views.DriverPreviousTrip.as_view(), name = 'driver-trip-previous'),
    re_path(r'^driver/trip/aborted/$', views.DriverAbortTrip.as_view(), name = 'driver-trip-aborted'),
    
    re_path(r'^passenger/trip/$', views.PassengerTripListView.as_view(), name = 'driver-trip'),
    re_path(r'^passenger/trip/create/$', views.PassengerTripCreateView.as_view(), name = 'passenger-trip'),
    re_path(r'^passenger/trip/active/$', views.PassengerActiveTrip.as_view(), name = 'passenger-trip-active'),
    re_path(r'^passenger/trip/previous/$', views.PassengerActiveTrip.as_view(), name = 'passenger-trip-previous'),
    re_path(r'^passenger/trip/abort/$', views.PassengerAbortTrip.as_view(), name = 'passenger-trip-abort'),
]

