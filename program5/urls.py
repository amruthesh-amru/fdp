from django.urls import path
from .views import register_student, course_detail,create_student,create_course
app_name = 'program5'
urlpatterns = [
    path('register_student/', register_student, name='register_student'),
    path('course_detail/<int:course_id>/', course_detail, name='course_detail'),
    path('create_student/',create_student, name='create_student'),
    path('create_course/',create_course, name='create_course')
]