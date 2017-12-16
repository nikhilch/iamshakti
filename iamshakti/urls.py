from django.conf.urls import *
from . import views

urlpatterns = [
    url('', views.index, name='index'),
]

#urlpatterns = patterns('',
#    url('', views.index, name='index')
#);
