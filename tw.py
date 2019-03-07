from email.utils import parsedate
from time import strftime
from twitter import *

# -----------------------------------------------------------------------
# load our API credentials
# -----------------------------------------------------------------------
import sys
sys.path.append(".")
import config

# -----------------------------------------------------------------------
# create twitter streaming API object
# -----------------------------------------------------------------------
auth = OAuth(config.access_key,
             config.access_secret,
             config.consumer_key,
             config.consumer_secret)
stream = TwitterStream(auth=auth, secure=True)

# -----------------------------------------------------------------------
# iterate over tweets
# -----------------------------------------------------------------------
tweet_iter = stream.statuses.sample()

for tweet in tweet_iter:
    try:
        if tweet["lang"] == "en":
            # turn the date string into a date object that python can handle
            timestamp = parsedate(tweet["created_at"])

            # now format this nicely into HH:MM:SS format
            timetext = strftime("%H:%M:%S", timestamp)

            print("%s" % (timetext), tweet["text"])
    except:
        continue
