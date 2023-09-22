from django.db import models

class Lizard (models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    discription = models.TextField(max_length=250)
    size = models.IntegerField()
    