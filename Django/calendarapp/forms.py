from django import forms
from django.forms import DateTimeInput
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['EventName', 'EventDate', 'EventType', 'EventCategory', 'Description']
    # Add a DateTimeInput widget for the EventDate field
    EventDate = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        help_text='Format: YYYY-MM-DD HH:MM',
    )

