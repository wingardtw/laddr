from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import (
    Endorsement,
    Endorsements,
    LaddrMatch,
    Profile,
    UserMatch,
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
            'playstyle',
            'role',
            'goal',
            'rank',
            'is_real',
            'endorsements',
        )
        read_only_fields = (
            'num_profiles_ranked',
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


class UserMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMatch
        fields = (
            'uuid',
            'from_user',
            'to_user',
            'message',
            'rejected_at',
            'viewed_at',
        )
        read_only_fields = (
            'rejected_at',
            'viewed_at',
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

    # def validate(self, data):
    #     if data.get('endorser') == data.get('endorsee'):
    #         raise serializers.ValidationError("Cannot endorse yourself")
    #     return data

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
