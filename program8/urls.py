from django.urls import path
from .views import StudentListView, StudentDetailView

urlpatterns = [
 path('program8/', StudentListView.as_view(), name='student-list'),
 path('program8/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]