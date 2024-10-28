from django.db import models


# Create your models here.
class Sleep(models.Model):
    date = models.DateField()
    sleep_duration = models.FloatField()
    sleep_quality = models.CharField(max_length=50)


class Exercise(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=50)
    duration = models.FloatField()


class Diet(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=50)
    calories = models.IntegerField()
