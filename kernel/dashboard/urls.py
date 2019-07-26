from django.urls import include
from django.urls import path
from django.urls import re_path

from . import views
from users import views as user_views
from trip import views as trip_views


app_name = 'dashboard'
urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
    re_path(r'^support/$', views.SupportView.as_view(), name='support'),
    # re_path(r'^reset-password/$', views.ResetPasswordView.as_view(), name='reset_password'),
    re_path(r'^favorite-routes/$', views.FavoriteRoutesView.as_view(), name='favorite_routes'),
    re_path(r'^favorites/$', views.FavoritesView.as_view(), name='favorites'),
    re_path(r'^notifications/$', views.NotificationView.as_view(), name='notifications'),
    re_path(r'^faq/$', views.FAQView.as_view(), name='faq'),
    re_path(r'^rules/$', views.RulesView.as_view(), name='rules'),
    re_path(r'^passenger/$', views.PassengerHomeView.as_view(), name='passenger'),
    re_path(r'^driver/$', views.DriverHomeView.as_view(), name='driver'),

    re_path(r'^driver/profile/', user_views.ProfileDriver.as_view(), name='driver-profile'),
    re_path(r'^driver/trip/$', trip_views.DriverTripListView.as_view(), name = 'driver-trip'),
    re_path(r'^driver/trip/create/$', trip_views.DriverTripCreateView.as_view(), name = 'driver-trip-create'),
    re_path(r'^driver/trip/active/$', trip_views.DriverActiveTrip.as_view(), name = 'driver-trip-active'),
    re_path(r'^driver/trip/previous/$', trip_views.DriverPreviousTrip.as_view(), name = 'driver-trip-previous'),
    re_path(r'^driver/trip/aborted/$', trip_views.DriverAbortTrip.as_view(), name = 'driver-trip-aborted'),

    re_path(r'^passenger/profile', user_views.ProfilePassenger.as_view(), name='passenger-profile'),
    re_path(r'^passenger/trip/$', trip_views.PassengerTripListView.as_view(), name = 'passenger-trip'),
    re_path(r'^passenger/trip/create/$', trip_views.PassengerTripCreateView.as_view(), name = 'passenger-trip-create'),
    re_path(r'^passenger/trip/active/$', trip_views.PassengerActiveTrip.as_view(), name = 'passenger-trip-active'),
    re_path(r'^passenger/trip/previous/$', trip_views.PassengerPreviousTrip.as_view(), name = 'passenger-trip-previous'),
    re_path(r'^passenger/trip/abort/$', trip_views.PassengerAbortTrip.as_view(), name = 'passenger-trip-aborted'),
]
