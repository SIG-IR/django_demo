from __future__ import unicode_literals

from django.db import models

class State(models.Model):
    abbreviation = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=25, unique=True)

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    
class Tweet(models.Model):
    text = models.CharField(max_length=140)
    author = models.CharField(max_length=100)
    sentiment = models.DecimalField(max_digits=5, decimal_places=2)
    state = models.ForeignKey(State)
    candidate = models.ForeignKey(Candidate)