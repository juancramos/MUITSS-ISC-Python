import twitter
import json

# -----------------------------------------------------------------------
# load our API credentials
# -----------------------------------------------------------------------
import sys
import config
PROJECT_PATH = config.data_directory

# -----------------------------------------------------------------------
# create twitter streaming API object
# -----------------------------------------------------------------------
auth = twitter.OAuth(config.access_key,
             config.access_secret,
             config.consumer_key,
             config.consumer_secret)
stream = twitter.TwitterStream(auth=auth, secure=True)

# -----------------------------------------------------------------------
# iterate over tweets
# -----------------------------------------------------------------------
tweet_iter = stream.statuses.sample()
alltweets = []

for tweet in tweet_iter:
    try:
        if(len(alltweets) > config.max_count):
            break
        if tweet["lang"] == "en" and tweet["place"] != None and tweet["place"]["country_code"] == "US":
            alltweets.append(tweet)
    except:
        continue

print("Total tweets downloaded %s" % (len(alltweets)))

with open('{}/{}.json'.format(PROJECT_PATH, "tweets"), 'w', encoding='utf8') as jsonFile:
    json.dump(alltweets, jsonFile)