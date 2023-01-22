from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator 
from user.models import User
import random

def randId():
    return random.randint(100001, 999999)




class Party(models.Model):
    id = models.IntegerField("party id", primary_key=True, validators=[MinValueValidator(100000), MaxValueValidator(999999)], default=randId )
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.TextField()

class Member(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)

class Vote(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    placeid = models.CharField(blank=True, null=False, max_length=100)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)


