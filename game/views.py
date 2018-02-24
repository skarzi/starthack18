from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.parsers import JSONParser

from game.models import UserScore
from game.serializers import UserScoreSerializer


class UserScoresList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = UserScore.objects.all()
    serializer_class = UserScoreSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        print(data)
        (score, new) = UserScore.objects.get_or_create(user_id=data['user_id'])
        score.score = data['score']
        score.save()
        return JsonResponse(UserScoreSerializer(UserScore.objects.get(user_id=data['user_id'])).data)
