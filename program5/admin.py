from django.contrib import admin
from .models import Course
from .models import Student

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
