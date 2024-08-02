from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import StudentForm, ProjectForm


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the student list or another appropriate view
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the project list or another appropriate view
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'program7/add_project.html', {'form': form})


def project_list(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    return render(request, 'program7/project_list.html', {'projects': projects})


def project_detail(request, pk):
    # Fetch a single project by its primary key or return 404
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'program7/project_detail.html', {'project': project})

# Create your views here.
