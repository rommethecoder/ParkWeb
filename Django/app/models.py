from django.db import models

# Create your models here.
class UserRole(models.Model):
    UserRoleID = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=30)

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserRoleID = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Phone = models.CharField(max_length=15, null=True)