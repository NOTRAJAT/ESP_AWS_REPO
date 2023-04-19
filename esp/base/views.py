

from django.http import HttpResponse
from django.shortcuts import render
from base.models import esp
# Create your views here.


def home(request):

    # return render(request, 'home.html')
    return render(request, "index.html")


def state_0(request):
    output = esp.objects.filter(id=1).update(state=0)
    return HttpResponse("ok_0")


def state_1(request):
    output = esp.objects.filter(id=1).update(state=1)

    return HttpResponse("ok_1")


def status_get(request):
    output = esp.objects.get(pk=1)
    if(output.state):
        return HttpResponse(1)
    else:
        return HttpResponse(0)


def analog_put(request, value):
    esp.objects.filter(id=1).update(analog=value)
    return HttpResponse("1")


def analog_get(request):
    response = esp.objects.get(pk=1)

    return HttpResponse((response.analog))
