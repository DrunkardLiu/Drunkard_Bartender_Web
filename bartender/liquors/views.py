from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
#
# def hello_world(request):
#     return HttpResponse("Hello World!")


from datetime import datetime
from django.shortcuts import render

from .models import BaseLiquor

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def home(request):
    baseLiquor_list = BaseLiquor.objects.all()
    return render(request, 'home.html', {
        'baseLiquor_list': baseLiquor_list,
    })
