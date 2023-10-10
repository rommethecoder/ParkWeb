from django.urls import path, include
from django.contrib import admin
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path('admin/', admin.site.urls),
    path('calendar/', include('calendarapp.urls')),
]
