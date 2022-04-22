from django.db import models

# Create your models here.
class Pomodoro(models.Model):
    excercise   = models.IntegerField()
    rest        = models.IntegerField()
    sets        = models.IntegerField()