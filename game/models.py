from django.db import models

from users.models import User


class UserScore(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    score = models.IntegerField()
