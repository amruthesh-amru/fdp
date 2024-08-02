from django.contrib import admin
from .models import Student, Project

admin.site.register(Project)

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1  # Specifies the number of extra forms to display

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ProjectInline]

admin.site.register(Student, StudentAdmin)

# Register your models here.
