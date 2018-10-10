from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from api.models import (
    Availability,
    Match,
    Membership,
    Profile,
    PsychePreference,
    Psychograph,
    Team,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')


class ProfileSerializer(serializers.ModelSerializer):
    #Ending point: Need to figure out how to use the SlugRelatedField. What would this be for us? Something unique...
    #Do not need to use a SlugRelatedField. Instead, can just force a user to be made before the profile gets made. Just need to make a user view and such. 
    
    #user = serializers.SlugRelatedField(
    #    slug_field='username', queryset=User.objects.all()
    #)
    
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
            'calibrator',
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


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        validators = [
            UniqueTogetherValidator(
                queryset=Match.objects.all(),
                fields=('player_a', 'player_b'),
            )
        ]
        fields = (
            'uuid',
            'player_a',
            'player_b',
            'player_a_accept',
            'player_b_accept',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
        )
