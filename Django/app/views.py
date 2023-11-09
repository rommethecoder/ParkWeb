from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from app.models import *
from datetime import datetime
import json
from django import forms
from django.forms import DateTimeInput


def homePage(request):
    context = {}
    return render(request, "home.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def map_calendarPage(request):
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

    # # For Map Items
    # eventsForMap = Event.objects.all()
    # event_data = []
    # for event in eventsForMap:
    #     event_data.append({
    #         'title': event.name,  # Use the correct field name from the model
    #         'start': event.date.isoformat(),
    #         'end': event.date.isoformat(),  # Assuming you want the end time to be the same as the start time
    #         'description': event.description,
    #     })

    context = {
        "areas": area,
        "events": event,
        "bookings": booking,
        "bookableAreas": bookableArea,
        "current_date": datetime.now(),
        # 'events_json': json.dumps(event_data)
    }

    return render(request, "map_calendar.html", context)


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


def create_event_and_booking(request):
    if request.method == 'POST':
        # Extract data from the form
        event_name = request.POST.get('event_name')
        event_date_str = request.POST.get('event_date')
        is_public = request.POST.get('is_public') == 'true'
        event_category = request.POST.get('event_category')
        event_description = request.POST.get('event_description')
        estimated_attendance = request.POST.get('attendance')
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')
        area_id = request.POST.get('area_id')
        user_id = request.user.id  # Assuming the user is logged in

        # Convert date and time strings to datetime objects
        event_date = datetime.strptime(event_date_str, '%Y-%m-%d').date()
        start_time = datetime.strptime(start_time_str, '%H:%M').time()
        end_time = datetime.strptime(end_time_str, '%H:%M').time()

        # Combine date and time to create datetime objects
        event_start_datetime = datetime.combine(event_date, start_time)
        event_end_datetime = datetime.combine(event_date, end_time)

        # Create Event object
        event = Event.objects.create(
            name=event_name,
            date=event_start_datetime,
            is_public=is_public,
            category=event_category,
            description=event_description
        )

        # Create Booking object
        booking = Booking.objects.create(
            start_time=event_start_datetime,
            end_time=event_end_datetime,
            attendance=estimated_attendance,
            area_id=area_id,
            event_id=event.id,
            user_id=user_id
        )

        # Return success response
        return redirect('map')
    else:
        return redirect('map')


def logoutUser(request):
    logout(request)
    return redirect('home')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'is_public', 'category', 'description']

    # Add a DateTimeInput widget for the EventDate field
    date = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        help_text='Format: YYYY-MM-DD HH:MM',
    )


def get_events(request):
    events = Event.objects.all()
    event_data = []

    for event in events:
        if event.is_public:
            event_title = event.name
        else:
            event_title = "Private Event"
        event_data.append({
            'id': event.id,
            'title': event_title,
            'date': event.date,
            'category': event.category,
            'description': event.description,
        })

    return JsonResponse(event_data, safe=False)
