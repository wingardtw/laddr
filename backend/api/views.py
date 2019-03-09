from django.contrib.auth.models import User
from rest_framework import viewsets
import api.serializers as serializers
from api.models import (
    Endorsement,
    Endorsements,
    LaddrMatch,
    Profile,
    UserMatch,
)
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class LaddrMatchViewSet(viewsets.ModelViewSet):
    queryset = LaddrMatch.objects.all()
    serializer_class = serializers.LaddrMatchSerializer


class UserMatchViewSet(viewsets.ModelViewSet):
    queryset = UserMatch.objects.all()
    serializer_class = serializers.UserMatchSerializer


class EndorsementViewSet(viewsets.ModelViewSet):
    queryset = Endorsement.objects.all()
    serializer_class = serializers.EndorsementSerializer


class EndorsementsViewSet(viewsets.ModelViewSet):
    queryset = Endorsements.objects.all().order_by('endorsee')
    serializer_class = serializers.EndorsementsSerializer

def endorsement_view(request):
    user = request.user
    player_b = request.data.player_b
    user_profile = user.Profile
    player_b_profile = player_b.Profile
    user_profile.endorse_player(player_b_profile,request.data.endorsement)