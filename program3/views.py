from django.shortcuts import render
from .models import Student

def display_lists(request):
    fruits = ['Apple','Banana','Cherry','Date']
    students = Student.objects.all()
    return render(request, 'program3/display_list.html',{'fruits': fruits,'students': students})


