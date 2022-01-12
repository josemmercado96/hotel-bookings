from django.urls import path
from bookings import views


urlpatterns = [
    path('', views.list_booking),
    path('<int:pk>/pay/', views.pay_booking),
    path('<int:pk>/cancel/', views.cancel_booking)
]
