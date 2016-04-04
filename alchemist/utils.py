import json
import random
import os
def get_random_alchemy_credentials():
    alchemy_api_keys = json.loads(os.environ['ALCHEMY_API_KEYS'])
    random.shuffle(alchemy_api_keys)
    return alchemy_api_keys