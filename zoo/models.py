from django.db import models

# Create your models here.
from django.utils.encoding import smart_text


class Location(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return smart_text(self.name)


class Dragon(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    fav_food = models.CharField(max_length=40)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return smart_text(self.name)
