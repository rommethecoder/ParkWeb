from django.urls import path
from .import views

urlpatterns = [
    path("", views.homePage, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
]
