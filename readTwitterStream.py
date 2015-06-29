#!/usr/bin/env python


import json, io, sys, csv, optparse, time
"""
OVERVIEW: reads a json file of tweets as output by catchtwitterstream.py
and extracts the ones with coordinate info, writing the coordinates out to a file,
one per line, as well as the tweet timestamp, and an individual ID to allow
uniquely binding to SVG objects via D3.
"""

p = optparse.OptionParser()
p.add_option('-i', '--fin', dest = 'inputfile')
options, arguments = p.parse_args()

inputfile = options.inputfile
outputfile = inputfile[0:-5] + "Coords.txt"

tweets_data_path = inputfile
locations = []
numLines = 0
letter = inputfile[0] #for unique code
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        numLines += 1
        t = time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))
        c = tweet['coordinates']
        if c:
            c = c['coordinates'] #actually located at tweet['coordinates']['coordinates']
        if c is not None:
        	locations.append([c[0], c[1], t, numLines])
    except:
        continue
print "Number of tweets processed: ", numLines
print "Number of tweets with coordinates: ", len(locations)

f = open(outputfile, 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(["long", "lat", "time", "code"]) #code is uniqueID
    for location in locations:
        if location[2] > 1434529744:
            writer.writerow(location)
finally:
    f.close()