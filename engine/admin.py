from django.contrib import admin
from models import State, Candidate, Tweet

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    pass