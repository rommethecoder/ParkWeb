from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
import json
from django.http import JsonResponse

def calendar_view(request):
    events = Event.objects.all()

    event_data = []
    for event in events:
        event_data.append({
            'title': event.EventName,  # Use the correct field name from the model
            'start': event.EventDate.isoformat(),
            'end': event.EventDate.isoformat(),  # Assuming you want the end time to be the same as the start time
            'description': event.Description, 
        })

    context = {
        'events_json': json.dumps(event_data),
    }

    return render(request, 'calendarapp/calendar.html', context)

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()  # Save the event to the database
            event_data = {
                'id': event.EventID,  # Use the correct field name for the event ID
                'title': event.EventName,
                'start': event.EventDate.isoformat(),
                'end': event.EventDate.isoformat(),  # Assuming you want the end time to be the same as the start time
                'description': event.Description,
            }
            return redirect('calendar_view')
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = EventForm()
    return render(request, 'calendarapp/add_event.html', {'form': form})

def get_events(request):
    events = Event.objects.all()
    event_data = []

    for event in events:
        event_data.append({
            'id': event.EventID,
            'title': event.EventName,
            'start': event.EventDate.isoformat(),
            'end': event.EventDate.isoformat(),
            'description': event.Description,
        })

    return JsonResponse(event_data, safe=False)