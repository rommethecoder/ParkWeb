from app.models import User
from django.db import models


# Bookable Area Entity
class BookableArea(models.Model):
    AreaID = models.AutoField(primary_key=True)
    AreaName = models.CharField(max_length=30)
    Location = models.CharField(max_length=255)
    Capacity = models.IntegerField()

# Event Entity
class Event(models.Model):
    EventID = models.AutoField(primary_key=True)
    EventName = models.CharField(max_length=30, default="Default Event")
    EventDate = models.DateTimeField(default="2023-10-23 00:00:00")
    EventType = models.CharField(max_length=20, default="Default Type")
    EventCategory = models.CharField(max_length=30, default="Default Category")
    Description = models.TextField(default="Default Description")

# Availability Entity
class Availability(models.Model):
    AvailabilityID = models.AutoField(primary_key=True)
    AreaID = models.ForeignKey(BookableArea, on_delete=models.CASCADE)
    StartDateTIme = models.DateTimeField()
    EndDateTime = models.DateTimeField()
    IsAvailable = models.BooleanField(default=True)

# Booking Entity
class Booking(models.Model):
    BookingID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    EventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    AreaID = models.ForeignKey(BookableArea, on_delete=models.CASCADE)
    StartDateTime = models.DateTimeField()
    EndDateTime = models.DateTimeField()
