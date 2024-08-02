from django.urls import path
from program4.views import layout, home, about, contact
urlpatterns = [
    path('layout/', layout),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
