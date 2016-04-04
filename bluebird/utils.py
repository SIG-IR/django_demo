import json
import random
import os

def get_random_twitter_credentials():
    twitter_codes = json.loads(os.environ['TWITTER_API_KEYS'])
    random.shuffle(twitter_codes)
    return twitter_codes