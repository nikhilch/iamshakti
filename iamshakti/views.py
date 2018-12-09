from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


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

def stories(request):
    template = loader.get_template('stories.html')
    context = {
        None : None,
    }
    return HttpResponse(template.render(context, request))

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
