from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('initiatives/', views.initiatives, name='initiatives'),
    path('stories/', views.all_stories, name='all_stories'),
    path('stories/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.story_detail, name='story_detail'),
    path('resources/', views.resources, name='resources'),
    path('jointhemovement/', views.jointhemovement, name='jointhemovement'),
    path('donate/', views.donate, name='donate'),

    path('api/jtm/', views.JTMUser_list),
    path('api/jtm/<int:pk>', views.JTMUser_detail),
]
