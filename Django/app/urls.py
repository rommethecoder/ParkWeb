from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path("", views.homePage, name="home"),
    path("about/", views.about, name="about"),
    path('admin/', admin.site.urls),
    path("map/", views.mapPage, name="map"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path('create_event_and_booking/', views.create_event_and_booking, name='create_event_and_booking'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('calendar/add/', views.add_event, name='add_event'),
    path('calendar/get_events/', views.get_events, name='get_events'),
]

urlpatterns += staticfiles_urlpatterns()
