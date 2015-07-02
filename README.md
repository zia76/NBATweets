## NBATweets
Final project for Udacity Data Visualization Course: collect tweets during the NBA finals and map them using D3.

####Summary
I wanted to combine data munging techniques with visualization, so I created a pipeline that allows me to:
- catch tweets from the twitter streaming API matching a given search query, output in json (catchTwitterStream.py)
- filter the tweets for those containing GPS coordinate information (readTwitterStream.py)
- output the coordinate information in csv to be read in D3
- interactively visualize tweets on a global map using D3/JS/HTML (index.html)

As an example use of this pipeline, I collected tweets matching 3 queries during the last game of the 2015 NBA finals on June 16th. The queries were: 'Warriors', 'Cavaliers', and 'NBAfinals'. The visualization includes buttons to select each search term, and when pressed, you can watch the tweets appear on the map chronologically as the game proceeded.

*json tweet files not included here as they take up 3.4GB. Warriors5.json is the first 5 tweets for query "Warriors" for example.

####Design
The focus, scope and design of this project went through a lot of changes. Originally I was collecting tweets from different US states and analyzing their sentiment, then mapping state sentiment as a chloropleth. That project got hung up on technical grounds: I found that far less than 1% of tweets contain coordinate information for mapping. Given that the twitter RESTful API caps results at 100 per request, and caps requests at 15 per 15-minute window, It would have taken an unreasonable amount of time to collect enough geo-located tweets on all 50 states. My other option for collecting large numbers of tweets was to use the streaming API, but I would need to choose an upcoming event with a known time and for which I could predict popular hashtags. This is how I settled upon mapping tweets during the NBA Finals.

In terms of design, I used Mike Bostock's off-the-shelf world map, which came in a nice muted grey that would serve as a good background for the data. I matched the title, button and legend font colors to the map. I then looked up the official hexadecimal colors for the Warriors and Cavaliers jerseys and used those for the respective data points. For the #NBAFinals data, I chose the color of a basketball.



####Feedback


####Resources
I made heavy use of Mike Bostock's D3 documentation and examples generally, in particular:

http://d3-geomap.github.io/map/choropleth/world/

I obviously needed to read the twitter API docs:

https://dev.twitter.com/overview/documentation

I used this page for help figuring out the twitter API package for python:

https://rawgit.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition/master/ipynb/html/__Chapter%201%20-%20Mining%20Twitter%20(Full-Text%20Sampler).html

and a great blog post that really helped me with the python tweepy library that I finally chose after exploring 3 or 4 different twitter API libraries:

http://adilmoujahid.com/posts/2014/07/twitter-analytics/

I also read Scott Murray's book "Interactive Data Visualization" cover to cover to get a handle on D3.
