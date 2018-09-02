from django.conf.urls import url
from django.urls import path, include
from rest_framework.authtoken import views as drf_views
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"profiles", views.ProfileViewSet)
router.register(r"teams", views.TeamViewSet)
router.register(r"availability", views.AvailabilityViewSet)
router.register(r"psychepreferences", views.PsychePreferenceViewSet)
router.register(r"psychographs", views.PsychographViewSet)

app_name = 'api'
urlpatterns = [
    path("", include(router.urls)),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
    url(r'^calibrate$', views.calibrate, name='calibrate'),
    url(r'^get_matches/(?P<user_id>\d+)$', views.get_matches, name='get_matches'),
]
