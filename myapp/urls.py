from django.urls import path
from .views import AppointmentView

urlpatterns = [
    path('appointments/', AppointmentView.as_view(), name='appointments'),
    path('appointments/<int:pk>/', AppointmentView.as_view(), name='appointment-update'),
]
