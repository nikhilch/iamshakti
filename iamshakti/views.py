from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Story
from .models import JTMUser
from .serializers import JTMUserSerializer


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

@csrf_exempt
def JTMUser_list(request):
    if request.method == 'GET':
        users = JTMUser.objects.all()
        serializer = JTMUserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JTMUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    return HttpResponse(status=400)

@csrf_exempt
def JTMUser_detail(request, pk):
    try:
        user = JTMUser.objects.get(pk=pk)
    except JTMUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = JTMUserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = JTMUserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

    return HttpResponse(status=400)
