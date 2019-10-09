from django.contrib import admin
from .models import Takeoff, Landing


admin.site.register(Takeoff)
admin.site.register(Landing)