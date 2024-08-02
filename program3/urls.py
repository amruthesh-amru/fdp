from django.urls import path
from program3.views import display_lists

urlpatterns = [
    path('lists/', display_lists),
]
