from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout
from .views import CatsViewSet
from rest_framework import routers


app_name = 'blogapp'

#Почти так же, как и на руби.
router = routers.DefaultRouter()
router.register(r'cat', CatsViewSet, base_name='api')

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^reg/$', views.register, name='register'),
    url(r'^cats/$', views.cats, name='cats'),
    url(r'^culc/$', views.culc, name='culc'),
    url(r'^resume/$', views.resume, name='resume'),
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^addCat/$', views.add, name='add'),
    url(r'^cats/delete/(?P<cat_id>[0-9]+)$', views.delete, name='delete'),
    url(r'^edit/(?P<cat_id>[0-9]+)$', views.edit, name='edit'),
    url(r'^bot/$', views.bot, name='bot'),
    url(r'^api/', include(router.urls)),
    url(r'^error/$', views.signUp_error),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),

]