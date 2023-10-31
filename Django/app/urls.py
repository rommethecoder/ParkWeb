from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path("", views.homePage, name="home"),
    path("about/", views.about, name="about"),
    path('admin/', admin.site.urls),
    path('calendar/', include('calendarapp.urls')),
    path("map/", views.mapPage, name="map"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path('create_event_and_booking/', views.create_event_and_booking, name='create_event_and_booking'),
]

urlpatterns += staticfiles_urlpatterns()
