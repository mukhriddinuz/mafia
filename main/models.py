from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
import datetime


class User(AbstractUser):
    bio = models.CharField(max_length=150)
    friends = models.ManyToManyField(to='User')
    all_games = models.IntegerField()
    win_games = models.IntegerField()
    lose_games = models.IntegerField()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Room(models.Model):
    name = models.CharField(max_length=150)
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    password = models.CharField(max_length=30, null=True, blank=True)
    bots = models.IntegerField(null=True, blank=True)
    players_numbers = models.IntegerField(default=4)
    players = models.ManyToManyField(to=User)

    def clean(self):
        if self.players_numbers >= 4 and self.players_numbers <= 50:
            raise ValidationError("Son xato")


class GameRound(models.Model):
    round_number = models.IntegerField()



