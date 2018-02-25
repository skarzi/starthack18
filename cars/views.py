import json

from channels import Group
from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from cars.consumers import CHANNEL_GROUP_CAR, MSG_UNLOCK, MSG_LOCK
from cars.models import Car, CAR_STATE_OCCUPIED, Trip, CAR_STATE_RESERVED, CAR_STATE_AVAILABLE
from cars.serializers import CarSerializer, TripSerializer
from users.models import User
from users.serializers import UserSerializer


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


class CarUnlock(generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def put(self, request, car_pk, user_pk, *args, **kwargs):
        car = Car.objects.get(pk=car_pk)
        user = User.objects.get(pk=user_pk)
        Group(CHANNEL_GROUP_CAR % str(car.pk)).send({"text": json.dumps({
            'type': MSG_UNLOCK,
            'user': json.dumps(UserSerializer(user).data)
        })})
        if not Trip.objects.filter(car=car, user_id=user_pk, endtime__isnull=True).exists():
            # no open trip for this user for this car
            raise NotFound("This car was not reserved by the user")
        car.state = CAR_STATE_OCCUPIED
        car.save()
        return Response(CarSerializer(car).data)


class CarLock(generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def put(self, request, car_pk, user_pk, *args, **kwargs):
        car = Car.objects.get(pk=car_pk)
        if Trip.objects.filter(car=car, endtime__isnull=True).exclude(user_id=user_pk).exists():
            # Other user has reserved the car
            raise NotFound("This car is not reserved by the current user")
        Group(CHANNEL_GROUP_CAR % str(car.pk)).send({"text": json.dumps({
            'type': MSG_LOCK
        })})
        return Response(CarSerializer(car).data)


class CarReserve(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def put(self, request, car_pk, user_pk, *args, **kwargs):
        car = Car.objects.get(pk=car_pk)
        user = User.objects.get(pk=user_pk)
        if car.state != CAR_STATE_AVAILABLE:
            raise NotFound("This car is not available")
        car.state = CAR_STATE_RESERVED
        car.save()
        trip = Trip(user=user, car=car)
        trip.save()
        return Response(TripSerializer(trip).data)


class CarLocation(mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def put(self, request, car_pk, *args, **kwargs):
        car = Car.objects.get(pk=car_pk)
        data = JSONParser().parse(request)
        car.location = data['location']
        car.save()
        return Response(CarSerializer(car).data)


def ws_car_test(request, pk):
    return render(request, 'cars/car.html')

