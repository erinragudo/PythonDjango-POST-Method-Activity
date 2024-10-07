from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_appointment, name='create_appointment'),
    # path('create/', views.create_appointment, name='create_appointment'),
]
