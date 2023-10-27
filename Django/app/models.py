from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)

    objects = models.Manager();

    def __str__(self):
        return str(self.user)

    class Meta:
        managed = True
        db_table = 'userprofile'


class Area(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()

    objects = models.Manager();

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = 'area'


class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    is_public = models.BooleanField()
    category = models.CharField(max_length=30)
    description = models.TextField()

    objects = models.Manager();

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = 'event'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    attendance = models.IntegerField()

    objects = models.Manager();

    def __str__(self):
        return str(self.event.name) + " at " + str(self.area.name)

    class Meta:
        managed = True
        db_table = 'Booking'

