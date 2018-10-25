import random

from api.models import Team, Profile, PLAYSTYLES, ROLES, RANKS, Membership
from api.timezones import TIMEZONE_CHOICES
from django.contrib.auth.models import User
from django.utils.timezone import now


# faker import to generate fake data.
from faker import Faker

import csv

with open(
    r"C:\Users\Jacob\Documents\LaddrBase\laddr\backend\api\LolDuoCsv.csv", "r"
) as f:
    reader = csv.reader(f)
    bios = list(reader)


# First, define the fakegen function to generate the fake data.
fakegen = Faker()

# Then, we define our arrays of timezones, playstyles, roles, and ranks.
# timezones = ['PST','MST','CST','EST']
timezones = TIMEZONE_CHOICES
# playstyles =['Conservative','Competitive','Casual']
playstyles = PLAYSTYLES
role = ROLES
rank = RANKS


# The function to generate test users. Will generate 5x
# the number supplied (by default this is 10)
def populate_test_users(N=10):
    for entry in range(N * 5):
        uname = "Test_User_{0}".format(entry)
        if len(User.objects.filter(username=uname)) > 0:
            User.objects.get(username=uname).delete()
        user = User.objects.create(username=uname)

        fake_user = user
        fake_summoner = fakegen.word()
        fake_tz = random.choice(timezones)[0]
        fake_ps = random.choice(playstyles)[0]
        fake_fc = fakegen.safe_color_name()
        fake_bio = bios[entry]
        fake_role = random.choice(role)[0]
        fake_rank = random.choice(rank)[0]
        fake_jr = random.randint(0, 101)
        fake_sr = random.randint(0, 101)
        fake_tr = random.randint(0, 101)
        fake_pjr = random.randint(0, 101)
        fake_psr = random.randint(0, 101)
        fake_ptr = random.randint(0, 101)

        Profile.objects.get_or_create(
            user=fake_user,
            summoner_name=fake_summoner,
            timezones=fake_tz,
            playstyle=fake_ps,
            favorite_color=fake_fc,
            bio=fake_bio,
            role=fake_role,
            rank=fake_rank,
            is_real=False,
            johnny_rank=fake_jr,
            spike_rank=fake_sr,
            timmy_rank=fake_tr,
            preferred_johnny_rank=fake_pjr,
            preferred_spike_rank=fake_psr,
            preferred_timmy_rank=fake_ptr,
        )[0]

        Membership.objects.create(
            user=user,
            team=Team.objects.get(name="Test_Team_{0}".format(int(entry / 5))),
            date_joined=now(),
        )


# Function to create test teams to put users on.
# This must be run prior to the user population function
# in order to ensure that users have teams to be placed on.
def populate_test_teams(n=10):
    for i in range(n):
        tname = "Test_Team_{0}".format(i)
        if len(Team.objects.filter(name=tname)) > 0:
            Team.objects.get(name=tname).delete()
        Team.objects.create(name=tname, created_at=now(), is_real=False)


def populate(n=10):
    populate_test_teams(n)
    populate_test_users(n)
