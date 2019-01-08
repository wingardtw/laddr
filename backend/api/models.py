# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from backend.settings import DEFAULT_RANK_TOLERANCE

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

    @property
    def laddr_matches(self):
        return self.laddrmatch_player_a.all() | self.laddrmatch_player_b.all()

    @property
    def user_matches(self):
        return self.match_requests_received.all() | self.match_requests_received.all()

    @property
    def excluded_ids(self):
        """ Utility function for discerning unmatchable profiles"""
        matches = LaddrMatch.objects.filter(Q(player_a=self) | Q(player_b=self))
        matched_ids = set()

        # Always exclude admins
        for user in User.objects.filter(is_superuser=True):
            matched_ids.add(user.profile.uuid)

        # Don't match with existing matches
        for match in matches:
            # Should allow new match if old expired
            if not match.expired:
                matched_ids.add(match.player_a.uuid)
                matched_ids.add(match.player_b.uuid)

        # Don't match with existing partners
        for partner in DuoPartner.objects.filter(Q(player_a=self) | Q(player_b=self)):
            matched_ids.add(partner.player_a.uuid)
            matched_ids.add(partner.player_b.uuid)

        return list(matched_ids)

    def gen_match(self, store=True, use_rank=True, use_role=True, use_goal=True):
        matched_ids = self.excluded_ids
        filtered_matches = Profile.objects.exclude(uuid__in=matched_ids)
        primary_reason, secondary_reason, tertiary_reason = None, None, None

        # Random match first
        matched_profile = filtered_matches.first()
        primary_reason = "Random"

        # Try match based on goal


        # Try based on preference
        preference = self.matchingpreference

        # If role preference exists and want to filter by role
        if preference.role and use_role:
            print('Considering role')
            filtered_matches = filtered_matches.filter(role=preference.role)
            primary_reason = "Preferred role"

        # If rank preference exists and want to filter by rank
        if preference.rank and use_rank:
            print('Considering rank')
            floor = RANKS[0][0]
            ciel = RANKS[-1][0]

            if preference.rank - DEFAULT_RANK_TOLERANCE > floor:
                floor = preference.rank - DEFAULT_RANK_TOLERANCE
            if preference.rank + DEFAULT_RANK_TOLERANCE < ciel:
                ciel = preference.rank + DEFAULT_RANK_TOLERANCE

            print("Rank between {} and {}".format(RANKS[floor][0], RANKS[ciel][0]))

            filtered_matches = filtered_matches.filter(rank__range=[floor, ciel])
            if primary_reason:
                secondary_reason = "Preferred rank"
            else:
                primary_reason = "Preferred rank"

        #Add matching based on goal here, after filtering has been applied for other aspects.

        #The skeleton of this function would basically be to load in the current user's goal, and compare it against all other filtered user goals.
        #Then, you would sort the filtered_matches list by the goal similarity score. 
        # print("Considering goal")
        # nlp = spacy.load('en_core_web_md')

        # user_goal = self.goal
        # user_nlp=nlp(user_goal)
        # goallist = []

        # for p in filtered_matches:
        #    match_goal = p.goal
        #    match_nlp = nlp(match_goal)
        #    goal_sim = user_nlp.similarity(match_nlp)
        #    #now add profile uuid and similarity to an array as a tuple
        #    goal_tuple = (p.uuid, goal_sim)
        #    #append each tuple to the goal list
        #    goallist.append(goal_tuple)
      
        #Now we order the filtered matches by goal similarity score

        # mapping = dict(filtered_matches)
        # filtered_matches[:]=[(uuid,mapping[uuid]) for uuid in goallist]

        print(
            "{} possible matches left after filtering".format(len(filtered_matches))
        )
        matched_profile = filtered_matches.first()

        if not matched_profile:
            print('None found')
            return None

        # Finally create match object
        match = LaddrMatch(
            player_a=self,
            player_b=matched_profile,
            primary_reason=primary_reason,
            secondary_reason=secondary_reason,
            tertiary_reason=tertiary_reason,
        )

        if store:
            # Save the final match object
            match.save()

        return match

    def match_request(self, to_match, message=None):
        try:
            user_match = UserMatch(
                from_user=self,
                to_user=to_match,
                message=message,
            )
            user_match.save()
            return user_match
        except ValidationError as e:
            return e.message


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Connection(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player_a = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE,
        related_name='%(class)s_player_a',
    )
    player_b = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE,
        related_name='%(class)s_player_b',
    )

    # Metadata
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.player_a == self.player_b:
            raise ValidationError("Cannot connect with self")
        super(Connection, self).save(*args, **kwargs)


# class GoalRating(Connection):
#     score = models.DecimalField(default=0.0,decimal_places=3,max_digits=4)

#     def __str__(self):
#         return "%s is %f compatible with %s" % self.player_a, 100 * self.score, self.player_b

# @receiver(post_save, sender=Profile)
# def create_or_update_goal_mapping(sender, instance, created, **kwargs):
# #    if created:
# #        MatchingPreference.objects.create(player=instance)
# #    instance.matchingpreference.save()



class UserMatch(models.Model):
    """"User initiated matches"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_user = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE,
        related_name='match_requests_sent'
    )
    to_user = models.ForeignKey(
        "Profile",
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
        if self.from_user == self.to_user:
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

    @property
    def accepted(self):
        return self.player_a_accept and self.player_b_accept

    @property
    def rejected(self):
        a_rejected = self.player_a_rejected_at is not None
        b_rejected = self.player_b_rejected_at is not None
        if a_rejected:
            print("{} rejected at {}".format(
                self.player_a,
                self.player_a_rejected_at,
            ))
        if b_rejected:
            print("{} rejected at {}".format(
                self.player_b,
                self.player_b_rejected_at,
            ))
        return a_rejected or b_rejected

    @property
    def status(self):
        if self.expired:
            return "Expired"
        if self.accepted:
            return "Accepted"
        if self.rejected:
            return "Rejected"
        if self.player_a_accept:
            return "{} accepted, {} has yet to respond".format(
                self.player_a,
                self.player_b,
            )
        if self.player_b_accept:
            return "{} accepted, {} has yet to respond".format(
                self.player_b,
                self.player_a,
            )

    def __str__(self):
        return "Match between {} and {}".format(
            self.player_a.user.username, self.player_b.user.username
        )

    def save(self, *args, **kwargs):
        if self.player_a == self.player_b:
            raise ValidationError("Players cannot match themselves")
        super(LaddrMatch, self).save(*args, **kwargs)

    def accept(self, player):
        # Make sure player argument is player_a or player_b
        if self.player_a != player and self.player_b != player:
            raise ValidationError('This match does not have {}'.format(player))

        if self.expired:
            raise ValidationError('Match expired')

        # Logic for player a
        if player == self.player_a:

            # Ensure other player has not rejected already
            if self.player_b_rejected_at is not None:
                raise ValidationError("{} has already rejected".format(
                    self.player_b,
                ))

            if self.player_a_accept:
                return '{} already accepted. Waiting on {}'.format(
                    self.player_a,
                    self.player_b,
                )

            elif self.player_b_accept:
                print("Creating partnership")
                DuoPartner.objects.create(
                    player_a=self.player_a,
                    player_b=self.player_b,
                )
                print("Deleting Match object")
                self.delete()

            else:
                print("Updating match")
                self.player_a_accept = True
                self.player_a_accept_at = timezone.now()

        # Logic for player b
        elif player == self.player_b:

            # Ensure other player has not rejected already
            if self.player_a_rejected_at is not None:
                raise ValidationError("{} has already rejected".format(
                    self.player_a,
                ))
            if self.player_b_accept:
                return '{} already accepted. Waiting on {}'.format(
                    self.player_b,
                    self.player_a,
                )

            elif self.player_a_accept:
                print("Creating Partnership")
                DuoPartner.objects.create(
                    player_a=self.player_a,
                    player_b=self.player_b,
                )
                print("Deleting Match Object")
                self.delete()

            else:
                print("Updating match")
                self.player_b_accept = True
                self.player_b_accept_at = timezone.now()

        # Save match
        self.save()

    def reject(self, player):
        # Assert player is part of match
        if player != self.player_a and player != self.player_b:
            raise ValidationError(
                '{} is not associated with this match'.format(player)
            )

        # Do nothing to expired match
        if self.expired:
            raise ValidationError('Match expired')

        # Player a logic
        if player == self.player_a:
            self.player_a_accept = False
            self.player_a_accept_at = None
            self.player_a_rejected_at = timezone.now()

        # Player b logic
        elif player == self.player_b:
            self.player_b_accept = False
            self.player_b_accept_at = None
            self.player_b_rejected_at = timezone.now()

        # Save match
        self.save()


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
        return "{} -- Rank: {} -- Role: {}".format(
            self.player.user.username,
            self.get_rank_display(),
            self.get_role_display(),
        )


@receiver(post_save, sender=Profile)
def create_or_update_matching_preference(sender, instance, created, **kwargs):
    if created:
        MatchingPreference.objects.create(player=instance)
    instance.matchingpreference.save()
