from api.models import Profile
# from api.utility import exclude_matches
import spacy

def score_similarity(nlp, goal_a, goal_b):
    return nlp(goal_a).similarity(nlp(goal_b))

nlp = spacy.load('en_core_web_md')

for ProfileA in Profile.objects.all():
    for ProfileB in Profile.objects.all():
        if (ProfileA.uuid != ProfileB.uuid):
            score_similarity(nlp,ProfileA.goal,ProfileB.goal)



# Tiered matching. May use later.

# def find_match_tier_1(profile):
#     """ Finds a profile to serve as a potential tier 1 match
#         Tier 1 match is defined as a random match
#         @profile - api.models.Profile to be matched
#     """
#     matched_ids = exclude_matches(profile)
#     profiles = Profile.objects.exclude(uuid__in=matched_ids)
#     return profiles.first()


# def find_match_tier_2(profile):
#     """ Finds a profile to serve as a potential tier 2 match
#         Tier 2 match is based on similarity of goals
#         @profile - api.models.Profile to be matched
#     """
#     matched_ids = exclude_matches(profile)
#     profiles = Profile.objects.exclude(uuid__in=matched_ids)
#     return profiles
#     # LaddrMatch based on goal similarity


# def find_match_tier_4(profile):
#     """ Finds a profile to serve as a potential tier 4 match
#         Based on user's match preferences
#         @profile - api.models.Profile to be matched
#     """
#     matched_ids = exclude_matches(profile)
#     profiles = Profile.objects.exclude(uuid__in=matched_ids)
#     return profiles
#     # LaddrMatch based on profile similarity
