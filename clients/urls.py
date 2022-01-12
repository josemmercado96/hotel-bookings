from django.urls import path
from clients import views


urlpatterns = [
    path('', views.client_list),
]
