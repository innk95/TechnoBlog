from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

app_name = 'blogapp'

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^reg/$', views.register, name='register'),
    url(r'^cats/$', views.cats, name='cats'),
    url(r'^culc/$', views.culc, name='culc'),
    url(r'^error/$', views.signUp_error),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),

]