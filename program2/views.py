from django.shortcuts import render
from django.http import HttpResponse
import datetime
def offset_datetime(request):
    now=datetime.datetime.now()
    four_hours_later=now+datetime.timedelta(hours=4)
    four_hours_earlier=now-datetime.timedelta(hours=4)
    display = f"<html><body> Current date and time is {now} <br> Four hours later :{four_hours_later}<br> Four hours earlier :{four_hours_earlier}.</body></html>"
    return HttpResponse(display)



# Create your views here.
