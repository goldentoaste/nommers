from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator 
from user.models import User
import random

class RequestParam(models.Model):
    
    long = models.FloatField("longitude", blank=False, null=False, default=0)
    lat = models.FloatField("lattitude", blank=False, null=False, default=0)
    address = models.TextField("address", blank=True, null=False)
    radius = models.PositiveIntegerField("search radius (meters)", validators=[MaxValueValidator(50000)], default=1000)

    class SortBy(models.TextChoices):
        RELEVANCE = "R", "Relevance"
        DISTANCE = "D", "Distance"

    sortBy = models.CharField("sort option", choices=SortBy.choices, default=SortBy.RELEVANCE, max_length=20)

    class Cost(models.IntegerChoices):
        LOW = 1
        MED = 2
        HIGH = 3
        EXTRA = 4

    cost = models.IntegerField("max cost level", choices=Cost.choices, default=Cost.MED)
    
    


def randId():
    return random.randint(100001, 999999)



class Party(models.Model):
    id = models.IntegerField("party id", primary_key=True, validators=[MinValueValidator(100000), MaxValueValidator(999999)], default=randId )
    host = models.ForeignKey(User, on_delete=models.CASCADE)

