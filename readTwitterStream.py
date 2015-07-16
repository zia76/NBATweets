#!/usr/bin/env python


import json, io, sys, csv, optparse, time
"""
OVERVIEW: reads a json file of tweets as output by catchtwitterstream.py
and extracts the ones with coordinate info, writing the coordinates out to a file,
one per line, as well as the tweet timestamp, and an individual ID to allow
uniquely binding to SVG objects via D3.

python readTwitterStream.py -i Warriors.json
"""

p = optparse.OptionParser()
p.add_option('-i', '--fin', dest = 'inputfile')
options, arguments = p.parse_args()

inputfile = options.inputfile
outputfile = inputfile[0:-5] + "Coords.csv" #[0:-5] strips the .json ending
# a more flexible approach would be a regex that stripped any ending after the '.'

tweets_data_path = inputfile
locations = []

minTotalTime = 10000000000
maxTotalTime = 0
numLines = 0
numWithCoords = 0
numWithCoordsIncluded = 0

StartTime = 1434474625 #Unix timestamp for first timestamp to collect, hardcoded
EndTime = 1434515349 #Unix timestamp for last timestamp to collect, hardcoded
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        numLines += 1
        t = time.mktime(time.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y"))
        t -= 3600 * 7 #subtract 7 hours in seconds to convert UTC to Pacific Time
        if t < minTotalTime:
            minTotalTime  = t
        if t > maxTotalTime:
            maxTotalTime = t
        c = tweet['coordinates']
        if c:
            c = c['coordinates'] #actually located at tweet['coordinates']['coordinates']
        if c is not None:
            numWithCoords += 1
            if t >= StartTime and t <= EndTime:
                numWithCoordsIncluded += 1
                locations.append([c[0], c[1], t, numLines])

    except:
        continue

print "Number of tweets processed: ", numLines
print >> sys.stderr, "Earliest tweet in  data: ", minTotalTime
print >> sys.stderr, "Last tweet in  data: ", maxTotalTime
print "Number of tweets with coordinates: ", numWithCoords
print "Number of tweets with coordinates output: ", numWithCoordsIncluded

f = open(outputfile, 'wt')
try:
    writer = csv.writer(f)
    writer.writerow(["long", "lat", "time", "code"]) #code is uniqueID for data binding
    for location in locations:
            writer.writerow(location)
finally:
    f.close()