from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
#Test

def index(request):
    template = loader.get_template('ModeAppPage.html')
    return HttpResponse(template.render())


def happy(request):
    template = loader.get_template('HappyPage.html')
    HappyDatabase = happy_database.objects.all().values_list('id', 'author', "phrase", "authorPic")
    context = {
        'myDataBase': HappyDatabase,
    }
    return HttpResponse(template.render(context))

def sad(request):
    return HttpResponse("Hello, world. You're at the sad page.")

def angry(request):
    return HttpResponse("Hello, world. You're at the angry page.")

def nervous(request):
    return HttpResponse("Hello, world. You're at the nervous page.")




