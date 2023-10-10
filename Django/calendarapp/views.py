from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def calendar_view(request):
    events = Event.objects.all()
    return render(request, 'calendarapp/calendar.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = EventForm()
    return render(request, 'calendarapp/add_event.html', {'form': form})
