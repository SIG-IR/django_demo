"""
    seeder.py is the file that will initialize the database with static content, such as States and Candidates.
"""

import seed
from models import State, Candidate

def initialize_states():
    numStatesAdded = 0
    for abbrev in seed.states:
        obj, created = State.objects.get_or_create(abbreviation=abbrev, name=seed.states[abbrev])
        if created:
            numStatesAdded+=1
    print "New States Added: {}".format(numStatesAdded)
    print "States in Database: {}".format(State.objects.all().count())

def initialize_candidates():
    numCandidatesAdded = 0
    for cand in seed.candidates:
        obj, created = Candidate.objects.get_or_create(name=cand)
        if created:
            numCandidatesAdded+=1
    print "New Candidates Added: {}".format(numCandidatesAdded)
    print "Candidates in Database: {}".format(Candidate.objects.all().count())

def initialize():
    initialize_states()
    initialize_candidates()
    