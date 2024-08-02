from django.contrib import admin
from .models import Student,Course

admin.site.register(Student)

class CourseAdmin(admin.ModelAdmin):
    list_display=('name','list_students')

    def list_students(self,obj):
        return ", ".join([student.name for student in obj.students.all()])
    
admin.site.register(Course,CourseAdmin)
# Register your models here.
