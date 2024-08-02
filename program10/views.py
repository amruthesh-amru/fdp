from django.http import JsonResponse
from django.shortcuts import render
from .models import Student

from django.views.decorators.csrf import csrf_exempt
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@csrf_exempt
def register_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Student.objects.create(name=name)
        return JsonResponse({"message": "Student Registered Successfully"}, status=200)
    return render(request, 'program10/register_student.html')
    #return JsonResponse({"error": "Something went wrong"}, status=400)

def search_students(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('query')
        if query:
            students = Student.objects.filter(name__icontains=query).values('id', 'name')
            return JsonResponse(list(students), safe=False)
    return render(request, 'program10/search_student.html')
    #return JsonResponse({"error": "No data found"}, status=400)
