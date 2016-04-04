"""
    Extracts the sentiment of text using AlchemyAPI's service
"""
from alchemyapi import AlchemyAPI
import utils
def get_sentiment(text):
    alchemyapi = AlchemyAPI()
    for key in utils.get_random_alchemy_credentials():
        alchemyapi.apikey = key
        response = alchemyapi.sentiment("text", text)
        if 'docSentiment' not in response:
            continue
        return response['docSentiment'].get('score', '0')
