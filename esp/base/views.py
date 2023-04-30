

from turtle import position
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render, redirect
from base.models import esp
# Create your views here.


def home(request):
    if(request.method == "POST"):
        # return render(request, 'home.html')
        # data = request.POST("1")
        data = str(request.POST)
        position = data.find(']}>')
        value = int(data[position-2:position-1])
        esp.objects.filter(id=1).update(analog=value)
        print(value)

        return render(request, "index.html", {'val': value})
    
    output = esp.objects.get(pk=1)

    return render(request, "index.html", {'val': output.analog})


def seven_seg(request):
    pass


def state_0(request):
    output = esp.objects.filter(id=1).update(state=0)
    return HttpResponse("ok_0")


def state_1(request):
    output = esp.objects.filter(id=1).update(state=1)

    return HttpResponse("ok_1")


def status_get(request):
    output = esp.objects.get(pk=1)
    return HttpResponse(output.analog)


def analog_put(request, value):
    esp.objects.filter(id=1).update(analog=value)
    return HttpResponse("1")


def analog_get(request):
    response = esp.objects.get(pk=1)

    return HttpResponse((response.analog))
