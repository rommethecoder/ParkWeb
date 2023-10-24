from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path('add/', views.add_event, name='add_event'),
    path('get_events/', views.get_events, name='get_events'),
]
