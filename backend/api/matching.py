from api.models import Profile, LaddrMatch, MatchingPreference
from django.db.models import Q


def exclude_matches(profile):
    """ For a given profile, returns a list of profile ids to EXCLUDE from matching
        @profile - api.models.Profile to be matched
        Profiles are excluded if they are in an existing match with given profile
    """
    matches = LaddrMatch.objects.filter(Q(player_a=profile) | Q(player_b=profile))
    matched_ids = [
        *[x.player_a.uuid for x in matches],  # noqa: E999
        *[x.player_b.uuid for x in matches],
    ]
    return matched_ids


def filter_by_preference(profile):
    """ For a given profile, return a list of profild ids that satisfy
        criteria in that profile's preferences
    """
    if not MatchingPreference.objects.filter(player=profile).exists():
        return []
    matched_ids = exclude_matches(profile)
    new = Profile.objects.exclude(uuid__in=matched_ids)


def find_match_tier_1(profile):
    """ Finds a profile to serve as a potential tier 1 match
        Tier 1 match is defined as a random match
        @profile - api.models.Profile to be matched
    """
    matched_ids = exclude_matches(profile)
    profiles = Profile.objects.exclude(uuid__in=matched_ids)
    return profiles.first()


def find_match_tier_2(profile):
    """ Finds a profile to serve as a potential tier 2 match
        Tier 2 match is based on similarity of goals
        @profile - api.models.Profile to be matched
    """
    matched_ids = exclude_matches(profile)
    profiles = Profile.objects.exclude(uuid__in=matched_ids)
    # LaddrMatch based on goal similarity


def find_match_tier_3(profile):
    """ Finds a profile to serve as a potential tier 3 match
        Tier 3 match is based on user's calibration results
        @profile - api.models.Profile to be matched
    """
    matched_ids = exclude_matches(profile)
    profiles = Profile.objects.exclude(uuid__in=matched_ids)
    # LaddrMatch based on calibration
    x = [*['1'], *['2']]


def find_match_tier_4(profile):
    """ Finds a profile to serve as a potential tier 4 match
        Based on user's match preferences
        @profile - api.models.Profile to be matched
    """
    matched_ids = exclude_matches(profile)
    profiles = Profile.objects.exclude(uuid__in=matched_ids)
    preference = profile.matchingpreference
    # LaddrMatch based on profile similarity
