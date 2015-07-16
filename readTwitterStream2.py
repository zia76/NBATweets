#!/usr/bin/env python


import json, io, sys, csv, optparse, time
"""
OVERVIEW: similar to readTwitterStream.py:
reads a json file of tweets as output by catchtwitterstream.py
but extracts all tweets within a given time slice, not just the ones with coordinate info.
outputs to csv one tweet per line with timestamp

example: python readTwitterStream2.py -i Warriors.json > tweetTimes.csv
"""

p = optparse.OptionParser()
p.add_option('-i', '--fin', dest = 'inputfile')
options, arguments = p.parse_args()

inputfile = options.inputfile
tweets_data_path = inputfile
numLines = 0
numTweets = 0
tweetTimes = [];

collectionStartTime = 1434474625 #Unix timestamp
collectionEndTime = 1434515349 #Unix timestamp

tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        numLines += 1
        tweet = json.loads(line)
        t = time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))
        t -= 3600 * 7 #subtract 7 hours in seconds to convert UTC to Pacific Time

        if t >= collectionStartTime and t <= collectionEndTime:
            numTweets += 1
            tweetTimes.append([t])
    except:
        continue
print >> sys.stderr, "Number of tweets processed: ", numLines
print >> sys.stderr, "Number of tweets within the timeframe chosen: ", numTweets

writer = csv.writer(sys.stdout)
writer.writerow(["time"])
for time in tweetTimes:
    writer.writerow(time)