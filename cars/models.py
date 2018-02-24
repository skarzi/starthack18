from django.db import models
from location_field.models.plain import PlainLocationField

CAR_STATES = (
    ('available', 'Available'),
    ('reserved', 'Reserved'),
    ('occupied', 'Occupied'),
)


class Car(models.Model):
    model = models.CharField(max_length=100)
    location = PlainLocationField(based_fields=['city'], zoom=1)
    state = models.CharField(choices=CAR_STATES, max_length=20)

    def __str__(self):
        return "[%d] %s at %s" % (self.pk, self.model, self.location)
