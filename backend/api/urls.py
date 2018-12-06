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
router.register(r"laddrmatches", views.LaddrMatchViewSet)
router.register(r"endorsement", views.EndorsementViewSet)
router.register(r"endorsements", views.EndorsementsViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    url(r"^auth$", drf_views.obtain_auth_token, name="auth"),
    url(r"^calibrate$", views.calibrate, name="calibrate"),
]
