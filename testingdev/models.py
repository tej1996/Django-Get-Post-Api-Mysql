from django.db import models

# Create your models here.


class Info(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()

