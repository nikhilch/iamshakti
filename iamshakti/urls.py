from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('initiatives/', views.initiatives, name='initiatives'),
    path('stories/', views.all_stories, name='all_stories'),
    path('stories/<int:storyid>/', views.story_detail, name='story_detail'),
    path('resources/', views.resources, name='resources'),
    path('jointhemovement/', views.jointhemovement, name='jointhemovement'),
    path('donate/', views.donate, name='donate'),

]
