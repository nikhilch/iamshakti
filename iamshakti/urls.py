from django.conf.urls import *
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^initiatives/$', views.initiatives, name='initiatives'),
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^more/$', views.more, name='more'),
]
