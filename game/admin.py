from django.contrib import admin

from game.models import UserScore
from game.serializers import UserScoreSerializer


@admin.register(UserScore)
class UserScoreAdmin(admin.ModelAdmin):
    list_display = UserScoreSerializer.Meta.fields
