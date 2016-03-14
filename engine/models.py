from __future__ import unicode_literals

from django.db import models

# Author "has many" Books, and a Book "belongs to" a single 
# Author
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author)