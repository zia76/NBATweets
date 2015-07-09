#!/usr/bin/env python


import json, io, sys, csv, optparse, time
"""
OVERVIEW: similar to readTwitterStream.py:
reads a json file of tweets as output by catchtwitterstream.py
but extracts all tweets within a given time slice, not just the ones with coordinate info.
outputs to csv one tweet per line with timestamp and input file name:
this allows multiple json files to be processed and appended to the same csv, then loaded into d3
and using the file name as ID to group tweets for bar charts etc.

example: python readTwitterStream2.py -i Warriors.json >> tweetTimes.csv
"""

p = optparse.OptionParser()
p.add_option('-i', '--fin', dest = 'inputfile')
options, arguments = p.parse_args()

inputfile = options.inputfile
tweets_data_path = inputfile
numLines = 0
numTweetsDuringGame = 0
tweetTimes = [];

gameStartTime = 1434502799 #Unix timestamp for tipoff time
gameEndTime = 1434513601 #Unix timestamp for end of game

tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        numLines += 1
        tweet = json.loads(line)
        t = time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))
        if t > gameStartTime and t < gameEndTime:
            numTweetsDuringGame += 1
            tweetTimes.append([t, inputfile])
    except:
        continue
print >> sys.stderr, "Number of tweets processed: ", numLines
print >> sys.stderr, "Number of tweets during the game: ", numTweetsDuringGame

writer = csv.writer(sys.stdout)
writer.writerow(["time", "filename"])
for time in tweetTimes:
    writer.writerow(time)