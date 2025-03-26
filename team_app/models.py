from django.db import models
from django.urls import reverse
import pandas as pd

#
# Create your models here.

class Players(models.Model):

    objects = models.Manager()

    player = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.player


class FinesList(models.Model):

    objects = models.Manager()

    fine = models.CharField(max_length=50, unique=True)

    cost = models.IntegerField()

    def __str__(self):
        return self.fine

class PlayerFines(models.Model):

    objects = models.Manager()

    #table
    player_name = models.ForeignKey(Players, on_delete=models.CASCADE, default=1)

    player_fine = models.ForeignKey(FinesList, to_field='fine', on_delete=models.CASCADE)

    player_cost = models.IntegerField()

    player_paid = models.BooleanField(default=False)