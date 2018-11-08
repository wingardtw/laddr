# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .timezones import TIMEZONE_CHOICES
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.timezone import now
import uuid
import datetime

# Create your models here.
DEFAULT_MATCH_DURATION_DAYS = 30
DEFAULT_MATCH_EXPIRATION = now() + datetime.timedelta(days=DEFAULT_MATCH_DURATION_DAYS)

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
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    top_champions = JSONField(
        default=dict([("First", None), ("Second", None), ("Third", None)])
    )
    favorite_color = models.CharField(max_length=15, blank=False, null=True)
    bio = models.TextField(max_length=500, blank=True, null=False)
    role = models.CharField(max_length=15, choices=ROLES, null=True, blank=False)
    availability = JSONField(
        default=(
            [
                ("Monday", False),
                ("Tuesday", False),
                ("Wednesday", False),
                ("Thursday", False),
                ("Friday", False),
                ("Saturday", False),
                ("Sunday", False),
            ]
        )
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
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)


class Team(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(User, through="Membership")
    is_real = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Availability(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        date_format = "%A %H:%M"
        return "%s - %s" % (
            self.start.strftime(date_format),
            self.end.strftime(date_format),
        )


class PsychePreference(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("Profile", on_delete=models.CASCADE)
    psychograph = models.ForeignKey("Psychograph", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return "{uname} {accept} t:{tr} j:{jr} s:{sr}".format(
            uname=self.user.user.username,
            accept="accepts" if self.accepted else "rejects",
            tr=self.psychograph.timmy_rank,
            jr=self.psychograph.johnny_rank,
            sr=self.psychograph.spike_rank,
        )


class Psychograph(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    johnny_rank = models.IntegerField(default=0)
    spike_rank = models.IntegerField(default=0)
    timmy_rank = models.IntegerField(default=0)
    calibrator = models.BooleanField(default=False)

    class Meta:
        unique_together = ("johnny_rank", "timmy_rank", "spike_rank")


class SuggestedMatch(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player_a = models.ForeignKey(
        "Profile", on_delete=models.CASCADE, related_name="player_a"
    )
    player_b = models.ForeignKey(
        "Profile", on_delete=models.CASCADE, related_name="player_b"
    )
    player_a_accept = models.BooleanField(default=False)
    player_b_accept = models.BooleanField(default=False)
    a_accept_at = models.DateTimeField(default=None, null=True)
    b_accept_at = models.DateTimeField(default=None, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(default=DEFAULT_MATCH_EXPIRATION)
    partner = models.ForeignKey(
        "DuoPartner", on_delete=models.DO_NOTHING, null=True, default=None
    )


class DuoPartner(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player_a = models.ForeignKey(
        "Profile", on_delete=models.CASCADE, related_name="player_a"
    )
    player_b = models.ForeignKey(
        "Profile", on_delete=models.CASCADE, related_name="player_b"
    )
