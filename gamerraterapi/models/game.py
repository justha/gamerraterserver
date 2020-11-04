"""Game model module"""
from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    """Game database model"""
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    designer = models.CharField(max_length=50)
    year_released = models.DateField(auto_now=False, auto_now_add=False)
    number_of_players = models.IntegerField()
    est_play_time = models.TimeField(auto_now=False, auto_now_add=False)
    age_level = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)