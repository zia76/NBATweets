#!/usr/bin/env python
import optparse, sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

"""
OVERVIEW:  searches twitter streamingAPI for tweets about a particular query,
specified as option -q, and streams those tweets to stdout. pipe to a txt file
to read later.

ex: python catchTwitterStream.py -q Warriors > Warriors.json

**streams infdefinitely until halted with ctrl-c**
**must enter your own twitter credentials, mine not included :)**
"""

p = optparse.OptionParser()
p.add_option('-q', '--query', dest = 'queryString')
options, arguments = p.parse_args()

query = options.queryString
print >> sys.stderr, "query string is:", query

consumer_key = ##enter credentials here
consumer_secret = ##
access_token = ##
access_token_secret = ##

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=[query])
