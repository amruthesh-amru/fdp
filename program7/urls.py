from django.urls import path
from .views import add_project, project_detail, project_list

urlpatterns = [
    # URL for adding a new project
    path('add/', add_project, name='add_project'),
    # URL for listing all projects
    path('', project_list, name='project_list'),
    # URL for project details
    path('<int:pk>/', project_detail, name='project_detail'),
]
