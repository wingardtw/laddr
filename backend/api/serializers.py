from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Profile
        fields = (
            'uuid',
            'user',
            'summoner_name',
            'lol_server',
            'playstyle',
            'bio',
            'role',
            'rank',
            'is_real',
            'johnny_rank',
            'timmy_rank',
            'spike_rank',
            'preferred_johnny_rank',
            'preferred_timmy_rank',
            'preferred_spike_rank',
        )
