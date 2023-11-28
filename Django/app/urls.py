from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path("", views.homePage, name="home"),
    path('admin/', admin.site.urls),
    path("map_calendar/", views.map_calendarPage, name="map_calendar"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path('calendar/get_events/', views.get_events, name='get_events'),
    path('create_event_and_booking/', views.create_event_and_booking, name='create_event_and_booking'),
]

urlpatterns += staticfiles_urlpatterns()
