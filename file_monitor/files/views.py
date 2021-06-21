from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings as django_settings
import os
from faker import Faker
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

def index(request):
    if request.method == "GET":
        return render(request, "file_name.html")
    elif request.method == "POST":
        cds_keywords = [
            'SELECT','INNER JOIN','LEFT OUTER',
            'WHERE','HAVING','GROUP BY']
        print(request.method, request.POST, request.POST['file_name'])
        file = open(os.path.join(django_settings.STATIC_ROOT[0], request.POST['file_name']), 'w')
        file.write(Faker().text(ext_word_list=cds_keywords))
        file.close()
        return HttpResponse("File {} created !!".format(request.POST['file_name']))

