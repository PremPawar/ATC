from django.db import models
from django.core.validators import MinValueValidator

class Atc(models.Model):
    name            = models.CharField(max_length=200)
    runways         = models.PositiveSmallIntegerField(default=2)
    takeoff_limit   = models.PositiveSmallIntegerField(default=2)
    takeoffs        = models.PositiveSmallIntegerField(default=0)
    landing_limit   = models.PositiveSmallIntegerField(default=2)
    landings        = models.PositiveSmallIntegerField(default=0)
    created_at      = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at      = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Runway(models.Model):
    TAKEOFF = 0
    LANDING = 1
    TYPE_CHOICES = [
        (TAKEOFF, 'TAKEOFF'),
        (LANDING, 'LANDING'),
    ]
    atc             = models.ForeignKey(Atc, on_delete=models.CASCADE)
    is_used         = models.BooleanField(default=False)
    use             = models.PositiveSmallIntegerField(default=0, choices=TYPE_CHOICES)
    created_at      = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at      = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.atc.name + ' has runway #' + str(self.id) + ' for ' + str(self.use)

class Neighbour(models.Model):
    atc             = models.ForeignKey(Atc, on_delete=models.CASCADE, related_name='from_atc')
    atcto           = models.ForeignKey(Atc, on_delete=models.CASCADE, related_name='near_atc')
    distance        = models.DecimalField(decimal_places=2, max_digits=100, default=100.00, validators=[MinValueValidator(50)])
    created_at      = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at      = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active       = models.BooleanField(default=True)

    class Meta:
        unique_together = ("atc", "atcto")

    def __str__(self):
        return self.atc.name + ' has ' + self.atcto.name + ' near to it. @ distance ' + str(self.distance) + ' Kilometers' 
