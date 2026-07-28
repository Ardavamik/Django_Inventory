from django.shortcuts import render, loader
from django.http import HttpResponse

# Create your views here.
def app(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())