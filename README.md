## NBATweets
Final project for Udacity Data Visualization Course: collect tweets during the NBA finals and map them using D3.

####Summary
I wanted to combine data munging techniques with visualization, so I created a pipeline that allows me to:
- catch tweets from the twitter streaming API matching a given search query, output in json (catchTwitterStream.py)
- filter the tweets for those containing GPS coordinate information (readTwitterStream.py)
- output the coordinate information in csv to be read in D3
- interactively visualize tweets on a global map using D3/JS/HTML (index.html)

As an example, I collected tweets matching 3 queries during the last game of the 2015 NBA finals on June 16th. The queries were: 'Warriors', 'Cavaliers', and 'NBAfinals'. The visualization includes buttons to select each search term, and when pressed, you can watch the tweets appear on the map chronologically as the game proceeded.

*json tweet files not included here as they take up 3.4GB. Warriors5.json is the first 5 tweets for query "Warriors" for example.

####Resources
I made heavy use of Mike Bostock's D3 documentation and examples generally, in particular:

http://d3-geomap.github.io/map/choropleth/world/

I used this page for help figuring out the twitter API package for python:

https://rawgit.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition/master/ipynb/html/__Chapter%201%20-%20Mining%20Twitter%20(Full-Text%20Sampler).html

and a great blog post that really helped me with the python tweepy library that I finally chose after exploring 3 or 4 different twitter API libraries:

http://adilmoujahid.com/posts/2014/07/twitter-analytics/
