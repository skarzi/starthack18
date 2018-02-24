from rest_framework import serializers

from cars.models import Car, Trip


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'model', 'location', 'state')


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'user', 'car', 'starttime', 'endtime')