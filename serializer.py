import json
import secrets
# serialized_alchemy = '["{}"]'.format('", "'.join(str(x) for x in secrets.ALCHEMY_CODES))
print json.dumps(secrets.ALCHEMY_CODES)
print "\n\n"
print json.dumps(secrets.TWITTER_CODES)
print "\n\nCopy above into an environment variable with the below syntax: \n"
print "export ALCHEMY_API_KEYS = '{pasted text}'"