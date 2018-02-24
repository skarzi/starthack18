from django.contrib import admin

from cars.models import Car
from cars.serializers import CarSerializer


@admin.register(Car)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = CarSerializer.Meta.fields
