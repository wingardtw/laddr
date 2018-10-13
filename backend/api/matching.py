from api.models import Profile, Match
from django.db.models import Q


def exclude_matches(profile):
    """ For a given profile, returns a list of profile ids to EXCLUDE from matching
        @profile - api.models.Profile to be matched
        Profiles are excluded if they are in an existing match with given profile
    """
    matches = Match.objects.filter(Q(player_a=profile) | Q(player_b=profile))
    matched_ids = [
        *[x.player_a.uuid for x in matches],
        *[x.player_b.uuid for x in matches],
    ]  # flake8: noqa
    return matched_ids


def find_match_tier_1(profile):
    """ Finds a profile to serve as a potential tier 1 match
        @profile - api.models.Profile to be matched
    """
    matched_ids = exclude_matches(profile)
    profiles = Profile.objects.exclude(uuid__in=matched_ids)
    return profiles.first()


def find_match_tier_2(profile):
    """ Finds a profile to serve as a potential tier 2 match
        @profile - api.models.Profile to be matched
    """
    matched_ids = exclude_matches(profile)
    profiles = Profile.objects.exclude(uuid__in=matched_ids)
    # Match based on goal similarity

