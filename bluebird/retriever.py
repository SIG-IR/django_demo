"""
    Gets Tweets
"""
from TwitterAPI import TwitterAPI
import utils
import IPython
def get_tweets(query):
    for twitter_cred in utils.get_random_twitter_credentials():
        api = TwitterAPI(twitter_cred["CONSUMER_KEY"], twitter_cred["CONSUMER_SECRET"],
                    twitter_cred["ACCESS_TOKEN"], twitter_cred["ACCESS_SECRET"])
        request = api.request('search/tweets', {'q': query, 'lang': 'en','count': '100'})

        tweets = []

        # If keys were over used, move on
        if request.status_code == 403:
            continue

        # Append all tweets to array and return
        raw_json = request.json()['statuses']
        for tweet in raw_json:
            location = tweet['user'].get('location', '')
            if location == '':
                retweet = tweet.get('retweeted_status', '')
                if retweet != '':
                    location = retweet['user'].get('location', '')
            tweets.append({
                "text": tweet['text'],
                "location": location,
                "author": tweet['user'].get('name', 'None')
            })
        return tweets
    return None