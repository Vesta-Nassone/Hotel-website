from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_people = models.models.IntegerField()
    date = models.models.DateField()
    time = models.models.TimeField()


    def __str__(self):
        return self.name
    