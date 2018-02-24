from django.contrib import admin

from cars.models import Car, Trip
from cars.serializers import CarSerializer, TripSerializer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = CarSerializer.Meta.fields

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = TripSerializer.Meta.fields
