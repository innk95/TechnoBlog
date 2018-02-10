# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.db import models

# Create your models here.

class Cat(models.Model):
     user = models.ForeignKey(User, related_name='cats')
     name = models.CharField(max_length=40)
     years = models.IntegerField()
     breed = models.CharField(max_length=50)
     img = models.ImageField(default='static/images.default.jpg')





