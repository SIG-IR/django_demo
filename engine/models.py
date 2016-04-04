from __future__ import unicode_literals

from django.db import models

from django.db.models import Transform
from django.db.models import DecimalField

class AbsoluteValue(Transform):
    lookup_name = 'abs'
    function = 'ABS'

class State(models.Model):
    abbreviation = models.CharField(max_length=2, unique=False)
    name = models.CharField(max_length=25, unique=True)
    
    def __unicode__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    PARTY_CHOICES=(
        ('Democratic', 'Democratic'),
        ('Republican', 'Republican')
    )
    party = models.CharField(max_length=15, choices=PARTY_CHOICES)
    def __unicode__(self):
        return self.name
    
class Tweet(models.Model):
    text = models.CharField(max_length=155, blank=False, unique=True)
    author = models.CharField(max_length=100)
    sentiment = models.DecimalField(max_digits=5, decimal_places=2)
    state = models.ForeignKey(State) #state_id
    candidate = models.ForeignKey(Candidate) #candidate_id
    
    def __unicode__(self):
        return self.text
        
DecimalField.register_lookup(AbsoluteValue)