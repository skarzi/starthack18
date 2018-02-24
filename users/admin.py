# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from users.models import User
from users.serializers import UserSerializer


@admin.register(User)
class UserScoreAdmin(admin.ModelAdmin):
    list_display = UserSerializer.Meta.fields
