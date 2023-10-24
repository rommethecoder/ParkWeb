from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from app.models import Availability, Bookablearea, Booking, Event


def homePage(request):
    context = {}
    return render(request, "home.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def mapPage(request):
    availability = Availability.objects.all()
    area = Bookablearea.objects.all()
    bookable = Bookablearea.objects.raw(
        """
        SELECT * FROM bookablearea
        WHERE AreaID NOT IN (
            SELECT AreaID FROM booking
            )
        """
    )
    event = Event.objects.all()
    context = {
        "availabilities": availability,
        "areas": area,
        "bookableAreas": bookable,
        "events": event
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
