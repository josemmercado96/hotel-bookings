from django.urls import path
from room import views

urlpatterns = [
    path('', views.room_list)
]