import json

from channels import Group
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.parsers import JSONParser

from cars.models import Car, CAR_STATE_OCCUPIED
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
        car = Car.objects.get(pk=pk)
        Group('carsws' + str(pk)).send({"text": json.dumps(CarSerializer(car).data)})
        car.state = CAR_STATE_OCCUPIED
        car.save()
        # todo: register somewhere who is occupying the car
        return self.retrieve(request, *args, **kwargs)


def ws_car_test(request, pk):
    return render(request, 'cars/car.html')

