# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime as dt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

date = dt.datetime.today()


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "First name should be longer than 2 characters!"
            print "There is an error"
        if len(postData['username']) < 3:
            errors["username"] = "First name should be longer than 2 characters!"
            print "There is an error"
        if len(postData['password']) < 8:
            errors["password"] = "Password must be 8 characters"
            print "There is an error"
        if (postData['confirmation'] != postData['password']):
            errors["confirmation"] = "Passwords do not match"
            print "There is an error"
        return errors

class TripManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        print postData['from']

        if len(postData['destination']) < 1:
            errors["destination"] = "Destination should not be empty"
            print "There is an error"
        if len(postData['description']) < 1:
            errors["description"] = "Description should not be empty"
            print "There is an error"
        # if postData['from'] > postData['to']:
        #     print "There is an error"
        # if date > postData['from']:
        #     print "There is an error"


        
        


        return errors


class User(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


class Trip(models.Model):
    destination = models.CharField(max_length = 255)
    travelstart = models.DateField()
    travelend = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(User, related_name = "trips")
    users = models.ManyToManyField(User, related_name = "othertrips")
    objects = TripManager()



# Create your models here.
