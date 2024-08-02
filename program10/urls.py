from django.urls import path
from .views import  register_student, search_students

urlpatterns = [
    path('register_student/', register_student, name='register_student'),
    path('search_students/', search_students, name='search_students'),
]
