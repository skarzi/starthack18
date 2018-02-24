from rest_framework import serializers

from game.models import UserScore


class UserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScore
        fields = ('user_id', 'score')
        read_only_fields = ['pk']
