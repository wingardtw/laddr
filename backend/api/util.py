from api.models import (
    Profile,
    Psychograph,
    PsychePreference,
    User,
)
from api.serializers import ProfileSerializer


def pass_judgement_profile(profile_id, suggested_match_id, judgement):
    suggested_profile = Profile.objects.get(uuid=suggested_match_id)
    psychograph = Psychograph.objects.get_or_create(
        timmy_rank=suggested_profile.timmy_rank,
        johnny_rank=suggested_profile.johnny_rank,
        spike_rank=suggested_profile.spike_rank,
    )
    pass_judgement_psychograph(profile_id, psychograph, judgement)


def pass_judgement_psychograph(profile_id, psychograph, judgement):
    profile = Profile.objects.get(uuid=profile_id)
    PsychePreference.objects.create(
        user=profile,
        psychograph=psychograph,
        accepted=judgement,
    )


def gen_match(user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)
    profile_json = ProfileSerializer(profile).data
    return profile_json


def gen_matches(user_id, num_matches):
    matches = []
    for i in range(num_matches):
        matches.append(gen_match(user_id))
    return matches
