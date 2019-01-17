import random

from api.models import Profile, PLAYSTYLES, ROLES, RANKS
from django.contrib.auth.models import User
import spacy

# faker import to generate fake data.
from faker import Faker

import csv

with open(
    r"matching/LolDuoCsv.csv", "r"
) as f:
    reader = csv.reader(f)
    bios = list(reader)


# The function to generate test users. Will generate 6x
# the number supplied (by default this is 10)
def populate_test_users(N=10):
    fakegen = Faker()
    playstyles = PLAYSTYLES
    rank = RANKS
    role = ROLES

    for entry in range(N * 5):
        uname = "Test_User_{0}".format(entry)
        if len(User.objects.filter(username=uname)) > 0:
            User.objects.get(username=uname).delete()
        user = User.objects.create(username=uname)

        fake_user = user
        fake_summoner = fakegen.word()
        fake_ps = random.choice(playstyles)[0]
        fake_fc = fakegen.safe_color_name()
        fake_goal = bios[entry]
        if fake_goal[0] == '[' and fake_goal[-1] == ']':
            fake_goal = fake_goal.strip('\'[]')
        fake_role = random.choice(role)[0]
        fake_rank = random.choice(rank)[0]

        profile = Profile.objects.get(user=fake_user)

        profile.user = fake_user
        profile.summoner_name = fake_summoner
        profile.playstyle = fake_ps
        profile.favorite_color = fake_fc
        profile.goal = fake_goal
        profile.role = fake_role
        profile.rank = fake_rank
        profile.is_real = False

        profile.save()


def populate(n=10):
    populate_test_users(n)


def make_goal_matrix():
    profiles = [
        user.profile for user in User.objects.filter(profile__is_real=False)
    ]
    nlp = spacy.load('en_core_web_md')
    for p1 in profiles:
        for p2 in profiles:
            if p1 is not p2:
                p1_nlp = nlp(p1.goal)
                p2_nlp = nlp(p2.goal)
                score = p1_nlp.similarity(p2_nlp)
                new_rating = p1._rate_goal(p2, score, overwrite=True)
                print(new_rating)
