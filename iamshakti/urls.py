from django.conf.urls import url, patterns
from . import views

#urlpatterns = [
#    path('', views.index, name='index'),
#]

urlpatterns = patterns('',
    url('', views.index, name='index')
);
