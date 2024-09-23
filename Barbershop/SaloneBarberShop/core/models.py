from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class Person(models.Model):
    name = models.CharField(max_length=100)
    marks = models.CharField(max_length=100)

class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(max_length=100)


from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.service} on {self.date} at {self.time}"
