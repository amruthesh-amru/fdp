from django.shortcuts import render, redirect
from .models import Course, Student
from django.urls import reverse


def register_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        course_id = request.POST.get('course_id')
        student = Student.objects.create(name=student_name)
        course = Course.objects.get(id=course_id)
        course.students.add(student)
        return redirect(reverse('program5:course_detail', args=(course.id,)))
    courses = Course.objects.all()
    return render(request, 'program5/register_student.html', {'courses': courses})


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    return render(request, 'program5/course_detail.html', {'course': course, 'students': students})


def create_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student = Student.objects.create(name=student_name)
        Student.save(student)
    return render(request, 'program5/create_student.html')


def create_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        student_name = request.POST.get('student_name')
        student = Student.objects.get(name=student_name)
        course = Course.objects.create(name=course_name)
        course.students.set(student)
        Course.save(course)
    students = Student.objects.all()
    return render(request, 'program5/create_course.html', {'students': students})


# Create your views here.
