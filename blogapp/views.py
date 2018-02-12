# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import CatsSerializer
from .models import Cat
from .forms import CatCreationForm, PostForm

#Начальная страница, смотрит метод GET или POST
def index(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'index.html', {'form': form})
    else:
        form = PostForm(request.POST)
        message = request.POST.get('message')
        form.message = message
        if form.is_valid():
            form.save()
            return redirect('/')
        return redirect('/')

#вьюха регистрации
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

#Страница с котами.
def cats(request):
    if request.method == 'GET':
        current_user = request.user
        cats = Cat.objects.all();
        form = CatCreationForm()
        return render(request, 'cats.html', {'cats':cats, 'form': form, 'current_user':current_user})
    else:
        form = CatCreationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user  #добавляем хозяина к коту
            form.save()
            return redirect('/cats')
        else:
            return redirect('/cats')
#Страница с моим резюме
def resume(request):
    return render(request, 'resume.html')
#Калькулятор на питоне
def culc(request):
    return render(request, 'culc.html')
#Телеграм-бот. Надо бы найти ему хостинг
def bot(request):
    return render(request, 'bot.html')

def chat(request):
    return render(request, 'chat.html')
#Ещё не начал делать операции в фоне без перезагрузки
#Перекидываю на сраницу и передаю id кота
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
        form = CatCreationForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            current_cat.name = cat.name
            current_cat.years = cat.years
            current_cat.breed = cat.breed
            current_cat.img = cat.img
            current_cat.user = request.user
            current_cat.save()
        return redirect('/cats')

def add(request):
    if request.method == 'GET':
        form = CatCreationForm()
        return render(request, 'add.html', {'form': form})
    else:
        form = CatCreationForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.user = request.user
            cat.save()
        return redirect('/cats')
#Начало API
class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatsSerializer #сериализатор для обработки информации


#декоратор, который не пускает неавторизованных пользователей
@login_required
def signUp_error(request):
    return render(request, 'error.html')

@login_required
def login_error(request):
    return
