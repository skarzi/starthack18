from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.parsers import JSONParser

from game.models import UserScore
from game.serializers import UserScoreSerializer
from users.models import User


class UserScoresList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = UserScore.objects.all()
    serializer_class = UserScoreSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        (score, new) = UserScore.objects.get_or_create(user_id=data['user_id'])
        score.score = data['score']
        score.save()
        return JsonResponse(UserScoreSerializer(UserScore.objects.get(user_id=data['user_id'])).data)


class Leaderboard(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = UserScore.objects.order_by('-score')
    serializer_class = UserScoreSerializer

    def get(self, request, top, *args, **kwargs):
        ld = []
        for score in self.queryset[:int(top)]:
            user = User.objects.get(pk=score.user_id)
            ld.append({
                'name': user.name(),
                'age': user.age,
                'gender': user.gender,
                'score': score.score})
        return JsonResponse(ld, safe=False)


