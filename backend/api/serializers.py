from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import (
    Membership,
    Profile,
    Team,
)

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

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = (
            'user',
            'date_joined',
        )

class TeamSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Team
        fields = (
            'uuid',
            'name',
            'members',
            'created_at',
            'is_real',
        )
