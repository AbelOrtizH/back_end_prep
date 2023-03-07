#models.py/littlelemon
from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cook = models.CharField(max_length = 100)
    price = models.IntegerField()

    def __str__(self):
        return self.name + ' : ' + self.cuisine

class Logger(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default="adams")
    age = models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return f"{self.last_name}, {self.name}"

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField("Phone number", max_length=100)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"name:{self.name} - time:{self.time} - count: {self.count} - notes: {self.notes}"