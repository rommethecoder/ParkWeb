from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from app.models import *


def homePage(request):
    context = {}
    return render(request, "home.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def mapPage(request):
    area = Area.objects.all()
    event = Event.objects.all()
    booking = Booking.objects.all()

    bookableArea = Area.objects.raw(
        """
            SELECT * FROM area
            WHERE area.id NOT IN (
                SELECT booking.area_id
                FROM booking
            )
        """
    )

    context = {
        "areas": area,
        "events": event,
        "bookings": booking,
        "bookableAreas": bookableArea,
    }

    return render(request, "map.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username/password is incorrect !')

    context = {}
    return render(request, "login.html", context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was successfully created for ' + username)
                return redirect('login')

    context = {'form': form}
    return render(request, "register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
