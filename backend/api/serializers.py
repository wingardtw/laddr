from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import (
    Availability,
    Endorsement,
    Endorsements,
    LaddrMatch,
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
            'endorsements',
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


class LaddrMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaddrMatch
        fields = (
            'uuid',
            'player_a',
            'player_b',
            'player_a_accept',
            'player_b_accept',
            'created_at',
        )
        read_only_fields = (
            'created_at',
        )


class EndorsementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endorsement
        fields = (
            'uuid',
            'skill',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
        )


class EndorsementsSerializer(serializers.ModelSerializer):
    endorsee = ProfileSerializer(read_only=True)
    endorser = ProfileSerializer(read_only=True)
    skill = EndorsementSerializer(read_only=True)
    endorsee_ = serializers.PrimaryKeyRelatedField(
        source='endorsee',
        queryset=Profile.objects.all(),
    )
    endorser_ = serializers.PrimaryKeyRelatedField(
        source='endorser',
        queryset=Profile.objects.all(),
    )
    endorsement_ = serializers.PrimaryKeyRelatedField(
        source='endorsement',
        queryset=Endorsement.objects.all()
    )

    def validate(self, data):
        if data.get('endorser') == data.get('endorsee'):
            raise serializers.ValidationError("Cannot endorse yourself")
        return data

    class Meta:
        model = Endorsements
        fields = (
            'uuid',
            'endorsee',
            'endorser',
            'skill',
            'endorsee_',
            'endorser_',
            'endorsement_',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
        )
        extra_kwargs = {
            'endorsee_': {'write_only': True},
            'endorser_': {'write_only': True},
            'endorsement_': {'write_only': True},
        }
