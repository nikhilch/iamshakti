from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Story


def index(request):
    template = loader.get_template('index.html')
    context = {
        None : None,
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('about.html')
    context = {
        None : None,
    }
    return HttpResponse(template.render(context, request))

def initiatives(request):
    template = loader.get_template('initiatives.html')
    context = {
        None : None,
    }
    return HttpResponse(template.render(context, request))

def all_stories(request):
    latest_stories = Story.objects.all()
    context = { 'latest_stories' : latest_stories }
    return render(request, 'stories.html', context)

def story_detail(request, year, month, day, slug):
    story = get_object_or_404(Story, slug=slug, postdate__year=year, postdate__month=month, postdate__day=day)
    context = { 'story' : story }
    return render(request, 'story_detail.html', context)

def resources(request):
    template = loader.get_template('resources.html')
    context = {
        None : None,
    }
    return HttpResponse(template.render(context, request))

def jointhemovement(request):
    template = loader.get_template('jointhemovement.html')
    context = {
        None : None,
    }
    return HttpResponse(template.render(context, request))

def donate(request):
    template = loader.get_template('donate.html')
    context = {
        None : None,
    }
    return HttpResponse(template.render(context, request))
