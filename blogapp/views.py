# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def register(request):
    print('ok')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return redirect('/error')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'reg.html', context)

def cats(request):
    return HttpResponse('ke')

def culc(request):
    return render(request, 'culc.html')

@login_required
def signUp_error(request):
    return render(request, 'error.html')

@login_required
def login_error(request):
    return
