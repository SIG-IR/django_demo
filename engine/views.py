from django.shortcuts import render
from time import gmtime, strftime
import json
<<<<<<< HEAD
=======

def index(request):
    return render(request, 'engine/hello.html', {})

def add(request):
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    # Add a new model to the database
    a = Author(name='Author {}'.format(timestamp))
    a.save()
    b = Book(title='Book {}'.format(timestamp), author=a)
    b.save()
    return render(request, 'engine/all.html', {
        'authors' : Author.objects.all(),
        'books': Book.objects.all()
    })
>>>>>>> 970322abdc922b1a61fab5d8a54b3dffbe511926

def index(request):
    return render(request, 'engine/hello.html', {})