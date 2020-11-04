"""Image model module"""
from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    """Image database model"""
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)