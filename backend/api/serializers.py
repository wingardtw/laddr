from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import (
    Membership,
    Profile,
    Team,
    Availability,
    PsychePreference,
    Psychograph,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ProfileSerializer(serializers.ModelSerializer):
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
            'num_profiles_ranked',
            'johnny_rank',
            'timmy_rank',
            'spike_rank',
            'preferred_johnny_rank',
            'preferred_timmy_rank',
            'preferred_spike_rank',
        )
        read_only_fields = (
            'num_profiles_ranked',
        )


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = (
            'user',
            'date_joined',
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'uuid',
            'name',
            'members',
            'created_at',
            'is_real',
        )
        read_only_fields = (
            'created_at',
        )


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = (
            'uuid',
            'start',
            'end'
        )


class ProfilePsycheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'num_profiles_ranked',
            'johnny_rank',
            'timmy_rank',
            'spike_rank',
        )
        read_only_fields = (
            'num_profiles_ranked',
            'timmy_rank',
            'johnny_rank',
            'spike_rank',
        )


class PsychographSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psychograph
        fields = (
            'uuid',
            'created_at',
            'updated_at',
            'timmy_rank',
            'johnny_rank',
            'spike_rank',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
        )


class PsychePreferenceSerializer(serializers.ModelSerializer):
    psychograph = PsychographSerializer()

    class Meta:
        model = PsychePreference
        fields = (
            'uuid',
            'user',
            'psychograph',
            'created_at',
            'updated_at',
            'accepted'
        )
        read_only_fields = (
            'created_at',
            'updated_at',
        )
