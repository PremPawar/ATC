from django import forms
from django.contrib.auth.models import User
from flight.models import Path, Flight
from atc.models import Atc, Runway, Neighbour

class AddAtc(forms.ModelForm):
    class Meta:
        model = Atc
        fields = ['name', 'runways', 'takeoff_limit', 'landing_limit']
        widgets={
                   "name":forms.TextInput(attrs={'class':'form-control','required':'required'}),
                   "runways":forms.TextInput(attrs={'class':'form-control','required':'required'}),
                   "takeoff_limit":forms.TextInput(attrs={'class':'form-control','required':'required'}),
                   "landing_limit":forms.TextInput(attrs={'class':'form-control','required':'required'}),
            }
            
class AddRunway(forms.ModelForm):
    class Meta:
        model = Runway
        fields = ['atc', 'use']
        widgets={
                   "atc":forms.Select(attrs={'class':'form-control','required':'required'}),
                   "use":forms.Select(attrs={'class':'form-control','required':'required'}),
                }

class AddNear(forms.ModelForm):
    class Meta:
        model = Neighbour
        fields = ['atc', 'atcto','distance']
        widgets={
                   "distance":forms.NumberInput(attrs={'class':'form-control','required':'required'}),
                   "atc":forms.Select(attrs={'class':'form-control','required':'required'}),
                   "atcto":forms.Select(attrs={'class':'form-control','required':'required'}),
                }

class AddPath(forms.ModelForm):
    class Meta:
        model = Path
        fields = ['name', 'starting_atc','ending_atc','distance','time_required']
        widgets={
                   "name":forms.TextInput(attrs={'class':'form-control','required':'required'}),
                   "starting_atc":forms.Select(attrs={'class':'form-control','required':'required'}),
                   "ending_atc":forms.Select(attrs={'class':'form-control','required':'required'}),
                   "distance":forms.NumberInput(attrs={'class':'form-control','required':'required'}),
                   "time_required":forms.NumberInput(attrs={'class':'form-control','required':'required'}),
                }
        

class AddFlight(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'starting_atc','ending_atc','starting_time','expected_end','path']
        widgets={
                   "name":forms.TextInput(attrs={'class':'form-control','required':'required'}),
                   "starting_time":forms.TextInput(attrs={'class':'form-control','required':'required'}),
                   "expected_end":forms.TextInput(attrs={'class':'form-control','required':'required'}),
                   "starting_atc":forms.Select(attrs={'class':'form-control','required':'required'}),
                   "ending_atc":forms.Select(attrs={'class':'form-control','required':'required'}),
                   "path":forms.Select(attrs={'class':'form-control','required':'required'}),
                }