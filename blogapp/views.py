# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CatsSerializer
from .models import Cat
from .forms import CatCreationForm

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return render(request, 'error.html')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'reg.html', context)

def cats(request):
    if request.method == 'GET':
        current_user = request.user
        print(current_user)
        cats = Cat.objects.filter(user=current_user);
        return render(request, 'cats.html', {'cats':cats})


def culc(request):
    return render(request, 'culc.html')

def bot(request):
    return render(request, 'bot.html')

def chat(request):
    return render(request, 'chat.html')

def delete(request, cat_id):
    try:
        current_user = request.user
        current_cat = Cat.objects.get(id=cat_id)
        if current_user == current_cat.user:
            current_cat.delete()
            return redirect('/cats')
        return redirect('/cats')
    except:
        redirect('/cats')

def edit(request, cat_id=''):
    current_user = request.user
    current_cat = Cat.objects.get(id=cat_id)
    if not request.method == 'POST':
        form = CatCreationForm()
        if current_user == current_cat.user:
            return render(request, 'edit.html', {'cat': current_cat, 'form': form})
        else:
            return redirect('/cats')
    else:
        print(current_cat)
        form = CatCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/cats')

class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatsSerializer



@login_required
def signUp_error(request):
    return render(request, 'error.html')

@login_required
def login_error(request):
    return
