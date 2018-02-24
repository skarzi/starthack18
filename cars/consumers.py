import json
from datetime import datetime

from channels import Group
from channels.sessions import channel_session

from cars.models import Car, Trip, CAR_STATE_AVAILABLE
from game.models import UserScore

MSG_NEW_LOCATION_UPDATE = 'location_update'
MSG_UPDATE_SCORE = 'update_score'
MSG_TRIP_END = 'end_trip'
MSG_ENCOUNTER = 'encounter'

CHANNEL_GROUP_CAR = 'carws%s'


@channel_session
def ws_connect(message):
    # car is connecting
    message.reply_channel.send({"accept": True})
    label = int(message['path'].strip('/').split('/')[1])
    Group(CHANNEL_GROUP_CAR % str(label)).add(message.reply_channel)
    car = Car.objects.get(pk=label)
    message.channel_session['car_id'] = car.pk


@channel_session
def ws_receive(message):
    car = Car.objects.get(pk=message.channel_session['car_id'])
    data = json.loads(message['text'])
    if data['type'] == MSG_NEW_LOCATION_UPDATE:
        car.location = data['location']
        car.save()
        # todo: check if there are nearby cars
    elif data['type'] == MSG_UPDATE_SCORE:
        (score, new) = UserScore.objects.get_or_create(pk=int(data['user_id']))
        score.score = data['score']
        score.save()
    elif data['type'] == MSG_TRIP_END:
        trip = Trip.objects.get(car=car, endtime__isnull=True)
        trip.endtime = datetime.now()
        trip.save()
        trip.car.state = CAR_STATE_AVAILABLE
        trip.car.save()
    car = Car.objects.get(pk=message.channel_session['car_id'])
    Group(CHANNEL_GROUP_CAR % str(car.pk)).discard(message.reply_channel)


@channel_session
def ws_disconnect(message):
    car = Car.objects.get(pk=message.channel_session['car_id'])
    Group(CHANNEL_GROUP_CAR % str(car.pk)).discard(message.reply_channel)
