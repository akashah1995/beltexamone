# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages


def index(request):
    return render(request,'beltexamapp/index.html')

def travels(request):
    user = User.objects.get(id = request.session['loggedin'])
    tripinfo = user.trips.all().values()
    alltrips = Trip.objects.all().exclude(creator__id = request.session['loggedin'])

    context = {
        'information':tripinfo,
        'user':user,
        'alltrips':alltrips
    }


    return render(request, 'beltexamapp/travels.html', context)

def register(request):
    
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect(index)

    else: 
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(name = name, username = username, password = password)
        user = User.objects.get(username = username)
        request.session['loggedin'] = user.id
        return redirect(travels)

def addplan(request):
    return render(request, 'beltexamapp/addplan.html')


def login(request):
    username = request.POST['username']
    print username
    try:
        user = User.objects.get(username = username)
    except:
        messages.error(request, "Entered username is not in database", extra_tags = "loginerror")
        print "error"
        return redirect(index)

    if request.POST['password'] == user.password:
        request.session['loggedin'] = user.id
        return redirect(travels)

    else:
        messages.error(request, "Password is incorrect", extra_tags = "loginerror")
        print "error"
        return redirect(index)


def add(request):
    errors = Trip.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect(addplan)

    else: 
        destination = request.POST['destination']
        description = request.POST['description']
        datefrom = request.POST['from']
        dateto = request.POST['to']
        Trip.objects.create(destination = destination, description = description, travelstart = datefrom, travelend = dateto, creator = User.objects.get(id = request.session['loggedin']))
        
        # trip = Trip.objects.get(destination = destination)
        # trip.users.add(User.objects.get(id = request.session['loggedin']))

        return redirect(travels)

def destination(request,variable):
    trip = Trip.objects.get(id = variable)
    users = trip.users.values()

    context = {
        'trip':trip,
        'users':users
    }

    return render(request, 'beltexamapp/destination.html',context)


def join(request,variable):

    trip = Trip.objects.get(id = variable)

    user = User.objects.get(id = request.session['loggedin'])

    usersname = user.name
    
    for info in trip.users.all():
        if info.name == usersname:
            return redirect(travels)

# This ensure I don't add the same user twice
    
    trip.users.add(User.objects.get(id = request.session['loggedin']))

    trip.save()

    return redirect(travels)

    
# Create your views here.
