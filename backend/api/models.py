# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .timezones import TIMEZONE_CHOICES
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.timezone import now

# Create your models here.

LOL_SERVERS = (("NA", "North America"),)

PLAYSTYLES = (
    ("Aggressive", "Aggressive"),
    ("Conservative", "Conservative"),
    ("Supporting", "Supporting"),
)

ROLES = (
    ("Bottom", "Bottom"),
    ("Support", "Support"),
    ("Jungle", "Jungle"),
    ("Mid", "Mid"),
    ("Top", "Top"),
)
RANKS = (
    ("Bronze V", "Bronze V"),
    ("Bronze IV", "Bronze IV"),
    ("Bronze III", "Bronze III"),
    ("Bronze II", "Bronze II"),
    ("Bronze I", "Bronze I"),
    ("Silver V", "Silver V"),
    ("Silver IV", "Silver IV"),
    ("Silver III", "Silver III"),
    ("Silver II", "Silver II"),
    ("Silver I", "Silver I"),
    ("Gold V", "Gold V"),
    ("Gold IV", "Gold IV"),
    ("Gold III", "Gold III"),
    ("Gold II", "Gold II"),
    ("Gold I", "Gold I"),
    ("Platinum V", "Platinum V"),
    ("Platinum IV", "Platinum IV "),
    ("Platinum III", "Platinum III"),
    ("Platinum II", "Platinum II"),
    ("Platinum I", "Platinum I"),
    ("Diamond V", "Diamond V"),
    ("Diamond IV", "Diamond IV"),
    ("Diamond III", "Diamond III"),
    ("Diamond II", "Diamond II"),
    ("Diamond I", "Diamond I"),
    ("Challenger", "Challenger"),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    summoner_name = models.CharField(max_length=50, null=True, blank=False)
    lol_server = models.CharField(
        max_length=10, blank=False, choices=LOL_SERVERS, default="NA"
    )
    timezones = models.CharField(
        max_length=50, default="Etc/UTC", choices=TIMEZONE_CHOICES
    )
    playstyle = models.CharField(
        max_length=40, choices=PLAYSTYLES, default="Conservative"
    )
    top_champions = JSONField(default={"First": None, "Second": None, "Third": None})
    favorite_color = models.CharField(max_length=15, blank=False, null=True)
    bio = models.TextField(max_length=500, blank=True, null=False)
    role = models.CharField(max_length=15, choices=ROLES, null=True, blank=False)
    availability = JSONField(
        default={
            "Monday": False,
            "Tuesday": False,
            "Wednesday": False,
            "Thursday": False,
            "Friday": False,
            "Saturday": False,
            "Sunday": False,
        }
    )
    rank = models.CharField(max_length=15, choices=RANKS, blank=False, null=True)
    is_real = models.BooleanField(default=True)

    johnny_rank = models.IntegerField(default=0)
    spike_rank = models.IntegerField(default=0)
    timmy_rank = models.IntegerField(default=0)
    preferred_johnny_rank = models.IntegerField(default=0)
    preferred_spike_rank = models.IntegerField(default=0)
    preferred_timmy_rank = models.IntegerField(default=0)
    num_profiles_ranked = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def get_psyche(self):
        stats = {
            "Creative": self.johnny_rank,
            "Competitive": self.spike_rank,
            "Casual": self.timmy_rank,
        }
        return max(stats.keys(), key=(lambda key: stats[key]))


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    date_joined = models.DateField()


class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    date_created = models.DateField()
    members = models.ManyToManyField(User, through="Membership")
    is_real = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Availability(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        date_format = "%A %H:%M"
        return "%s - %s" % (start.strftime(date_format), end.strftime(date_format))


class NewsBlurb(models.Model):

    # A model for landing/home page cards

    text = models.TextField(max_length=500)
    date_created = models.DateField()
    date_posted = models.DateField()
    date_removed = models.DateField()
    active = models.BooleanField(default=False)
    in_rotation = models.BooleanField(default=False)
    is_primary = models.BooleanField(
        default=False
    )  # Marks Large primary card on landing


class PsychePreference(models.Model):
    user = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='%(class)s_preference')
    potential_match = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='%(class)s_offered_match')
    date_created = models.DateField(default=now)
    accepted = models.BooleanField(default=False)
