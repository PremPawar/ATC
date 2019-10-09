from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddAtc, AddRunway, AddNear, AddPath, AddFlight
from atc.models import Atc, Runway, Neighbour

@login_required
def add_atc(request, *args, **kwargs):
        if request.method == 'POST':
                form = AddAtc(request.POST or None, request.FILES or None)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.save()
                        messages.success(request, "Your post has been created")
                        return redirect("user")
        else:
                form = AddAtc()

        context = {
                'form': form,
        }
        return render(request, 'user/add_atc.html', context)

@login_required
def add_runway(request, *args, **kwargs):
        if request.method == 'POST':
                form = AddRunway(request.POST or None, request.FILES or None)
                if form.is_valid():
                        post = form.save(commit=False)
                        id = post.atc.id
                        atc = Atc.objects.get(id=id)
                        no_of_runways = atc.runways
                        runways = Runway.objects.filter(atc=atc)
                        if no_of_runways > runways.count():
                                post.save()
                                messages.success(request, "Runway Successfully Added")
                                return redirect("add_runway")
                        else:
                                messages.success(request, "Already " + str(runways.count()) + " runways are registered for same")
                                return redirect("add_runway")
        else:
                form = AddRunway()

        context = {
                'form': form,
        }
        return render(request, 'user/add_runway.html', context)

@login_required
def add_near(request, *args, **kwargs):
        if request.method == 'POST':
                form = AddNear(request.POST or None, request.FILES or None)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.save()
                        messages.success(request, "Your post has been created")
                        return redirect("user")
        else:
                form = AddNear()

        context = {
                'form': form,
        }
        return render(request, 'user/add_near.html', context)

@login_required
def add_path(request, *args, **kwargs):
        if request.method == 'POST':
                form = AddPath(request.POST or None, request.FILES or None)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.save()
                        messages.success(request, "Your post has been created")
                        return redirect("user")
        else:
                form = AddPath()

        context = {
                'form': form,
        }
        return render(request, 'user/add_path.html', context)

@login_required
def add_flight(request, *args, **kwargs):
        if request.method == 'POST':
                form = AddFlight(request.POST or None, request.FILES or None)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.save()
                        messages.success(request, "Your post has been created")
                        return redirect("user")
        else:
                form = AddFlight()

        context = {
                'form': form,
        }
        return render(request, 'user/add_flight.html', context)