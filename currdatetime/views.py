from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now =datetime.datetime.now()
    display = f"<html><body><h3> Current date and time is {now} .</h3></body></html>"
    return HttpResponse(display)

# Create your views here.
