from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.parsers import JSONParser

from cars.models import Car
from cars.serializers import CarSerializer


class CarsList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CarDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CarUnlock(mixins.RetrieveModelMixin,
                generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def put(self, request, pk, *args, **kwargs):
        # todo: have a websocket to the car here
        # todo: set this car to 'occupied'
        # todo: register somewhere who is occupying the car
        return HttpResponse("ok, unlocked " + str(pk))

