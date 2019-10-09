from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator
from atc.models import Atc


class Path(models.Model):
    name            = models.CharField(max_length=200)
    starting_atc    = models.ForeignKey(Atc, on_delete=models.CASCADE, related_name='path_starting_atc')
    ending_atc      = models.ForeignKey(Atc, on_delete=models.CASCADE, related_name='path_ending_atc')
    distance        = models.DecimalField(decimal_places=2, max_digits=100, default=100.00, validators=[MinValueValidator(50)])
    time_required   = models.CharField(max_length=10)
    fuel_required   = models.CharField(max_length=50)
    created_at      = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at      = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Flight(models.Model):
    IDLE = 0
    TAKEOFF_DONE = 1
    IN_AIR = 2
    EMERGENCY = 3
    LANDING = 4
    LANDED = 5
    TYPE_CHOICES = [
        (IDLE, 'IDLE'),
        (TAKEOFF_DONE, 'TAKEOFF_DONE'),
        (IN_AIR,'IN_AIR'),
        (EMERGENCY,'EMERGENCY'),
        (LANDING,'LANDING'),
        (LANDED,'LANDED'),
    ]
    name            = models.CharField(max_length=200)
    starting_atc    = models.ForeignKey(Atc, on_delete=models.CASCADE, related_name='starting_atc')
    ending_atc      = models.ForeignKey(Atc, on_delete=models.CASCADE, related_name='ending_atc')
    starting_time   = models.DateTimeField(default=datetime.now)
    expected_end    = models.DateTimeField(default=datetime.now)
    ending_time     = models.DateTimeField(default=datetime.now)
    path            = models.ForeignKey(Path, on_delete=models.CASCADE)
    height          = models.IntegerField(default=0)
    landing_type    = models.BooleanField(default=False)
    emergency_time  = models.DateTimeField(default=datetime.now, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at      = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active       = models.BooleanField(default=True)
    states          = models.PositiveSmallIntegerField(default=0, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name