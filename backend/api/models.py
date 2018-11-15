# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .timezones import TIMEZONE_CHOICES
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from backend.settings import DEFAULT_MATCH_EXPIRE

from constants import (
    RANKS,
    ROLES,
    SERVERS,
    PLAYSTYLES,
)

import uuid

# Create your models here.


class Profile(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    summoner_name = models.CharField(max_length=50, null=True, blank=True)
    server = models.CharField(
        max_length=10, blank=True, choices=SERVERS, default="NA"
    )
    timezones = models.CharField(
        max_length=50, default="Etc/UTC", choices=TIMEZONE_CHOICES
    )
    playstyle = models.CharField(
        max_length=40, choices=PLAYSTYLES, default="Conservative"
    )
    goal = models.TextField(max_length=200, blank=True, null=False)
    top_champions = JSONField(
        default={"First": None, "Second": None, "Third": None}
    )
    favorite_color = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=False)
    role = models.CharField(
        max_length=15, choices=ROLES, null=True, blank=True
    )
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
    rank = models.CharField(
        max_length=15, choices=RANKS, blank=True, null=True
    )
    is_real = models.BooleanField(default=True)

    johnny_rank = models.IntegerField(default=0)
    spike_rank = models.IntegerField(default=0)
    timmy_rank = models.IntegerField(default=0)
    preferred_johnny_rank = models.IntegerField(default=0)
    preferred_spike_rank = models.IntegerField(default=0)
    preferred_timmy_rank = models.IntegerField(default=0)
    num_profiles_ranked = models.IntegerField(default=0)
    endorsements = models.ManyToManyField(
        "Endorsement",
        through="Endorsements",
        through_fields=(
            'endorsee',
            'endorsement'
        )
    )

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
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)


class Team(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
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
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return '{uname} {accept} t:{tr} j:{jr} s:{sr}'.format(
            uname=self.user.user.username,
            accept='accepts' if self.accepted else 'rejects',
            tr=self.psychograph.timmy_rank,
            jr=self.psychograph.johnny_rank,
            sr=self.psychograph.spike_rank,
        )


class Psychograph(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    johnny_rank = models.IntegerField(default=0)
    spike_rank = models.IntegerField(default=0)
    timmy_rank = models.IntegerField(default=0)
    calibrator = models.BooleanField(default=False)

    class Meta:
        unique_together = ('johnny_rank', 'timmy_rank', 'spike_rank')


class Connection(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player_a = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_player_a',
    )
    player_b = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_player_b',
    )

    # Metadata
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.player_a == self.player_b:
            raise ValidationError("Cannot connect with self")
        super(Connection, self).save(*args, **kwargs)


class UserMatch(models.Model):
    """"User initiated matches"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='match_requests_sent'
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='match_requests_received'
    )

    message = models.TextField(_('Message'), blank=True)

    rejected_at = models.DateTimeField(blank=True, null=True)
    viewed_at = models.DateTimeField(blank=True, null=True)
    expired = models.BooleanField(default=False)
    expires_at = models.DateTimeField(default=DEFAULT_MATCH_EXPIRE)

    class Meta:
        verbose_name = _('User Match Request')
        verbose_name_plural = _('User Match Requests')
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return "%s" % self.from_user_id

    def save(self, *args, **kwargs):
        if self.player_a == self.player_b:
            raise ValidationError("Cannot request match with self")
        super(UserMatch, self).save(*args, **kwargs)


class LaddrMatch(Connection):
    """Matches created by Laddr"""
    player_a_accept = models.BooleanField(default=False)
    player_b_accept = models.BooleanField(default=False)
    primary_reason = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        default=None
    )
    secondary_reason = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        default=None
    )
    tertiary_reason = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        default=None
    )

    # Metadata
    player_a_accept_at = models.DateTimeField(auto_now=True)
    player_a_rejected_at = models.DateTimeField(blank=True, null=True)
    player_a_viewed_at = models.DateTimeField(blank=True, null=True)

    player_b_accept_at = models.DateTimeField(auto_now=True)
    player_b_rejected_at = models.DateTimeField(blank=True, null=True)
    player_b_viewed_at = models.DateTimeField(blank=True, null=True)

    expired = models.BooleanField(default=False)
    expires_at = models.DateTimeField(default=DEFAULT_MATCH_EXPIRE)

    def __str__(self):
        return "Match between {} and {}".format(
            self.player_a.user.username, self.player_b.user.username
        )

    def save(self, *args, **kwargs):
        if self.player_a == self.player_b:
            raise ValidationError("Players cannot match themselves")
        super(Endorsements, self).save(*args, **kwargs)


class DuoPartner(Connection):
    """Accepted matches"""
    player_a_feedback = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        default=None
    )
    player_b_feedback = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        default=None
    )
    player_a_rating = models.IntegerField(null=True, default=None)
    player_b_rating = models.IntegerField(null=True, default=None)
    suggested_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )  # If laddr suggested, this should be admin

    def __str__(self):
        return "Duo pair between {} and {}".format(
            self.player_a.user.username, self.player_b.user.username
        )


class Endorsement(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skill = models.CharField(max_length=20, blank=True, null=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill


class Endorsements(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    endorsement = models.ForeignKey("Endorsement", on_delete=models.CASCADE)
    endorser = models.ForeignKey(
        "Profile",
        related_name="endorser",
        on_delete=models.CASCADE
    )
    endorsee = models.ForeignKey(
        "Profile",
        related_name="endorsee",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('endorser', 'endorsee', 'endorsement')

    def save(self, *args, **kwargs):
        if self.endorser == self.endorsee:
            raise ValidationError("Cannot endorse self")
        super(Endorsements, self).save(*args, **kwargs)
