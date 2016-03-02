from django.shortcuts import render

def index(request):
    # Add a new model to the database
    
    # Fetch all from the database
    return render(request, 'engine/hello.html')