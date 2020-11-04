"""Review model module"""
from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """Review database model"""
    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)