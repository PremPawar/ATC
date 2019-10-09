from django.db import models
from django.core.validators import MinValueValidator
from atc.models import Runway
from flight.models import Flight

class Takeoff(models.Model):
    runway          = models.ForeignKey(Runway, on_delete=models.CASCADE, related_name='tekeoff_runway')
    flight          =  models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_takingoff')
    time            = models.DateTimeField()
    created_at      = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at      = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.runway.atc.name

class Landing(models.Model):
    runway          = models.ForeignKey(Runway, on_delete=models.CASCADE, related_name='landing_runway')
    flight          =  models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_landing')
    time            = models.DateTimeField()
    created_at      = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at      = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.runway.atc.name