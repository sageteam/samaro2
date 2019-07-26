from django.urls import include
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from .v1 import views

router = DefaultRouter()

router.register(r'login', views.APILoginViewSet, base_name='login')
router.register('users', views.UserViewSet)
router.register(r'feature', views.FeatureViewSet)
# 
router.register(r'city', views.CityViewSet)
router.register(r'region', views.RegionViewSet)
router.register(r'distance', views.DistanceViewSet)
router.register(r'feature', views.FeatureViewSet)
router.register(r'tickets', views.TicketViewSet)
router.register(r'ticket_message', views.TicketLetterViewSet)
router.register(r'rules', views.RulesViewSet)
router.register(r'rules_category', views.RulesCategoryViewSet)
router.register(r'faq', views.FAQViewSet)
router.register(r'faq_category', views.FAQCategoryViewSet)


app_name = 'api_v1'
urlpatterns = [
    re_path(r'v1/', include(router.urls)),
    re_path(r'v1/register/$', views.APIRegister.as_view(), name = 'user-registeration'),
    re_path(r'v1/user/profile/(?P<user>\d+)/$', views.APIRetrieveUpdateUserProfile.as_view(), name = 'user-profile'),
    re_path(r'v1/user/(?P<user>\d+)/favorites/$', views.APIFavoites.as_view(), name = 'api_user_favorites'),
    re_path(r'v1/user/(?P<user>\d+)/favorites/(?P<title>(\w+\s?)+)/$', views.APIFavoritesUpdate.as_view(), name = 'user-favorite-detail'),
    re_path(r'v1/user/profile/(?P<profile>\d+)/driver/$', views.APIRetrieveUpdateUserProfileDriver.as_view(), name = 'api_user_profile_driver'),
    re_path(r'v1/user/profile/(?P<driver>\d+)/machine/$', views.APIRetrieveUpdateUserMachine.as_view(), name = 'api_user_machine'),
    re_path(r'v1/user/profile/(?P<driver>\d+)/bank/$', views.APIRetrieveUpdateUserBank.as_view(), name = 'api_user_bank'),
    re_path(r'v1/user/profile/(?P<profile>\d+)/passenger/$', views.APIRetrieveUpdateUserProfilePassenger.as_view(), name = 'api_user_profile_passenger'),
    re_path(r'v1/user/profile/(?P<profile>\d+)/transmit/$', views.APIRetrieveUpdateUserProfilePassenger.as_view(), name = 'api_user_profile_transmit'),
    re_path(r'trips/$', views.APITripListCreate.as_view(), name = 'trips'),
    re_path(r'trips/user/(?P<user>\d+)/$', views.APIAllTripsUser.as_view(), name = 'user-trips'),
    re_path(r'trips/(?P<pk>\d+)/$', views.APITripRetrieveUpdate.as_view(), name = 'trips'),
    re_path(r'trip/(?P<pk>\d+)/seats/$', views.APISeatsATrip.as_view(), name = 'trip-seats'),
    re_path(r'trip/(?P<pk>\d+)/seat/(?P<pos>\d+)/$', views.APISeatsATripUpdate.as_view(), name = 'trip-seats-detail'),
]
