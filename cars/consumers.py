import asyncio

from channels import Group
from channels.sessions import channel_session
from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json

from cars.models import Car
from cars.serializers import CarSerializer


@channel_session
def ws_connect(message):
    # car is connecting
    message.reply_channel.send({"accept": True})
    label = int(message['path'].strip('/').split('/')[1])
    Group('carsws' + str(label)).add(message.reply_channel)
    car = Car.objects.get(pk=label)
    message.channel_session['car_pk'] = car.pk


@channel_session
def ws_disconnect(message):
    car = Car.objects.get(pk=message.channel_session['car_pk'])
    Group('carsws' + str(car.pk)).discard(message.reply_channel)



