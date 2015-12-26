from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def index(request):
#   return HttpResponse("Hello world")

def index(request):
  return render(request, 'pretotype/index.html')
