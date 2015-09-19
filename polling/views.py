from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
 if request.method == 'GET':
    return HttpResponse('I am called  from a get Request.')
 elif request.method == 'POST':
   return HttpResponse('I am calling from post Request')
# Create your views here.
