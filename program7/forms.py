from django import forms
from .models import Student, Project

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['topic', 'languages', 'duration', 'student']