from rest_framework import serializers

from game.models import UserScore
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField(read_only=True)

    def get_score(self, user):
        q = UserScore.objects.filter(user_id=user.pk)
        if q.exists():
            return q.first().score
        return 0

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'age', 'gender', 'created', 'score')
