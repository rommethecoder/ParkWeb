from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.homePage, name="home"),
    path("about/", views.about, name="about"),
    path("map/", views.mapPage, name="map"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
]

urlpatterns += staticfiles_urlpatterns()
