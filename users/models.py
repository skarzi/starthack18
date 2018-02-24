# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )



class User(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __repr__(self):
        return "%s [%s]" % (self.name, self.email)

    def __str__(self):
        return self.__repr__()

    class Meta:
        ordering = ('created',)
