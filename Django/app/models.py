from django.db import models

class Availability(models.Model):
    availabilityid = models.IntegerField(db_column='AvailabilityID', primary_key=True)  # Field name made lowercase.
    areaid = models.ForeignKey('Bookablearea', models.DO_NOTHING, db_column='AreaID')  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime')  # Field name made lowercase.
    isavailable = models.IntegerField(db_column='IsAvailable')  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'availability'


class Bookablearea(models.Model):
    areaid = models.IntegerField(db_column='AreaID', primary_key=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=30)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=255)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity')  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'bookablearea'


class Booking(models.Model):
    bookingid = models.IntegerField(db_column='BookingID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    eventid = models.ForeignKey('Event', models.DO_NOTHING, db_column='EventID')  # Field name made lowercase.
    areaid = models.ForeignKey(Bookablearea, models.DO_NOTHING, db_column='AreaID')  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime')  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'booking'


class Event(models.Model):
    eventid = models.IntegerField(db_column='EventID', primary_key=True)  # Field name made lowercase.
    eventname = models.CharField(db_column='EventName', max_length=30)  # Field name made lowercase.
    eventdate = models.DateTimeField(db_column='EventDate')  # Field name made lowercase.
    eventtype = models.CharField(db_column='EventType', max_length=20)  # Field name made lowercase.
    eventcategory = models.CharField(db_column='EventCategory', max_length=30)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'event'


class User(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    userroleid = models.ForeignKey('Userrole', models.DO_NOTHING, db_column='UserRoleID')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=30)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=30)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'user'


class Userrole(models.Model):
    userroleid = models.IntegerField(db_column='UserRoleID', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=30)  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'userrole'