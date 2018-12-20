# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from api.utility import default_match_expire

from constants import (
    RANKS,
    ROLES,
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
    playstyle = models.CharField(
        max_length=40, choices=PLAYSTYLES, default="Conservative"
    )
    goal = models.TextField(max_length=200, blank=True, null=False)
    favorite_color = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=False)
    role = models.CharField(
        max_length=15, choices=ROLES, null=True, blank=True
    )
    rank = models.IntegerField(choices=RANKS, blank=True, null=True)
    is_real = models.BooleanField(default=True)

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
    expires_at = models.DateTimeField(default=default_match_expire)

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


class MatchingPreference(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player = models.OneToOneField("Profile", on_delete=models.CASCADE)

    rank = models.IntegerField(choices=RANKS, blank=True, null=True)
    rank_importance = models.IntegerField(default=0)
    role = models.CharField(
        max_length=15, choices=ROLES, null=True, blank=True
    )
    role_importance = models.IntegerField(default=0)

    def __str__(self):
        return self.player.user.username
