from django.shortcuts import render
from time import gmtime, strftime
from engine.models import State, Tweet, Candidate
from django.http import HttpResponse
import json
from django.db.models import Count, Sum
from django.http import JsonResponse
import IPython
def index(request):
    states = State.objects.all()
    result = {}
    for s in states:
        state_name = str(s.name)
        tweets_in_state = Tweet.objects.filter(state=s).values('candidate_id').annotate(total=Count('candidate_id'), sentiment_total=Sum('sentiment')).order_by('total')
        sum_total = sum_democratic = sum_republican = max_democratic = max_republican = 0
        winner_democratic = winner_republican = ""
        for t in tweets_in_state: # Change candidate id to candidate name
            t['sentiment_total'] = float(t['sentiment_total'])
            c = Candidate.objects.get(pk=t["candidate_id"])
            t["candidate"] = str(c.name)
            t["party"] = str(c.party)
            sum_total += t["total"]
            if c.party.lower() == "democratic":
                sum_democratic += t["total"]
            else:
                sum_republican += t['total']
        result[str(s.abbreviation)] = {
            "details": list(tweets_in_state), # Convert QuerySet to list otherwise lots of formatting errors
            "total": sum_total,
            "democratic": sum_democratic,
            "republican": sum_republican,
            "name": state_name
        }
    # return JsonResponse(result)
    return render(request, 'engine/hello.html', {"data": result})

def state(request, state):
    s = State.objects.filter(abbreviation=state).first()
    sentimental_tweets = Tweet.objects.filter(state=s,sentiment__abs__gte=0.3).values('author', 'sentiment', 'text').order_by('sentiment')
    for tweet in sentimental_tweets:
        tweet['sentiment'] = float(tweet['sentiment'])
    return JsonResponse({'data': list(sentimental_tweets), 'state': s.name}, safe=False)