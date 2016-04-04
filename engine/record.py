from engine.models import State, Candidate, Tweet
from bluebird import retriever as bluebird
from alchemist import retriever as alchemist
from django.db import IntegrityError
from django.db.models import Q
def fetchAndStoreTweets():
    candidateTweets = 0
    for c in Candidate.objects.all():
        candidateTweets = 0
        tweets = bluebird.get_tweets(c.name)
        for tweet in tweets:
            if tweet["location"] == "":
                continue
            qset = Q()
            for term in tweet["location"].split():
                qset |= Q(name__contains=term) | Q(abbreviation__contains=term)    
            location = State.objects.filter(qset).first()
            if location == None:
                continue
            sentiment = alchemist.get_sentiment(tweet['text'])
            try:
                obj, created = Tweet.objects.get_or_create(text=tweet['text'], sentiment=sentiment, author=tweet['author'],state=location, candidate=c)
            except IntegrityError:
                continue
            if created:
                candidateTweets+=1
        print "New Tweets For {}: {}".format(c.name, candidateTweets)
    print "Total Tweets: {}".format(Tweet.objects.all().count())