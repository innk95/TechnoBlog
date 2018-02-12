# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Cat, Post

from django.contrib import admin

# Register your models here.

admin.site.register(Cat)
admin.site.register(Post)
