## NBATweets
Final project for Udacity Data Visualization Course: collect tweets during the NBA finals and map them using D3.

####Summary
I wanted to combine data munging techniques with visualization, so I created a pipeline that allows me to:
- catch tweets from the twitter streaming API matching a given search query, outputting tweets in json (catchTwitterStream.py)
- extract tweet timestamps (readTwitterStream2.py) and filter the tweets for those containing GPS coordinate information (readTwitterStream.py) and output the times/coordinates in csv,  and 
- load the tweet data into d3 and interactively visualize them on a global map (index.html)

As an example use of this pipeline, I collected tweets matching 3 queries during the last game of the 2015 NBA finals on June 16th. The queries were: 'Warriors', 'Cavaliers', and 'NBAfinals'. The visualization includes buttons to select each search term, and when pressed, you can watch the tweets appear on the map chronologically as the game proceeds.

####Design
The focus, scope and design of this project went through a lot of changes. Originally I was collecting tweets from different US states and analyzing their sentiment, then mapping state positivity as a choropleth. That project got hung up on technical grounds: I found that far less than 1% of tweets contain coordinate information for mapping. Given that the twitter RESTful API caps results at 100 per request, and caps requests at 15 per 15-minute window, it would have taken an unreasonable amount of time to collect enough geo-located tweets on all 50 states. My other option for collecting large numbers of tweets was to use the streaming API, but I would need to choose an upcoming event with a known time and for which I could predict popular hashtags. This is how I settled upon mapping tweets during the NBA Finals.

In terms of design, I used Mike Bostock's off-the-shelf world map, which came in a nice muted grey that would serve as a good background for the data. I matched all font color to the map. I then looked up the official hexadecimal colors for the Warriors and Cavaliers jerseys and used those for the respective data points. For the #NBAFinals data, I chose the color of a basketball.

I played around with how to represent each tweet on the map, starting with simple points, then experimenting with things like infinitely expanding circles centered at each tweet location. I wanted the tweets to appear with some amount of motion in order to call attention to newly-emerging points. The endlessly expanding rings centered at each tweet location were artful and visually cool, but distracted from the core communication. Ultimately, I settled on expanding but quickly disappearing circles to call attention to new points, with a persistent dot in the center to mark each tweet. I think this was a reasonable way to make use of viewers' pre-attentive processing, create an exciting visualization, and ultimately still communicate the main message (where in the world people were tweeting about the game).

Although beta users found their way through the interactivity without need for guidance, I added a small note of instruction just to be safe, and made sure it disappeared once the animation began so as not to distract visually.

Originally there was no timeline below the map. I received feedback that this would be a nice feature, so I added one. Ideally, the ball representing time would be draggable to allow users to pause, fast-forward and rewind through the data. I plan to implement this feature eventually, but since pausing and resuming are not built-in functionality within d3, adding this feature, particularly resuming, is more complicated than I had expected, and a bit beyond my d3 comfort-level currently.


####Feedback
User 1 thought the data point sizes were confusing. Intuitively, he thought areas with greater tweet density should have larger circles, which is to say, he thought I should be using circle radius to encode tweet density. He then realized that such an encoding wasn't naturally compatible with using a single point of standard radius for each tweet, without aggregation across geographic area. Still, his feedback was that by using data points of noticeable radius/area I was implying using area as an encoding for tweet density, thus his confusion, whereas the use of a more point-like circle would not imply such an encoding. I responded by reducing the radii of the data points, though I kept them at a 4px radius because visually I didn't like going any smaller (I had been using 5-8px radius).

This user also suggested adding a time legend to indicate the game's progress during the animation. Without a legend, users had a relative sense of the passage of time, but no absolute knowledge of where they were in the game. In response, I added a time legend.

User 2 was also confused as to what a single dot represented. He assumed (correctly) that a dot was a single tweet, but he wasn't sure, and suggested a legend (I added a note to clarify). He also thought it would be cool and natural if the animation could be paused or advanced by hand. I completely agree, but this feature ended up being a little too technically involved for this project, as discussed above.

User 3 liked the animation but wanted some kind of summary statistics or quantification of the data. I responded by adding a few stats as text in the Pacific and Indian Oceans.

The main critique in the review of my first project submission was that the visualization was exploratory not explanatory: it did not communicate a particular trend or draw a clear conclusion from the data. This was an entirely fair point. I didn't want to completely throw out my map, so I added a histogram underneath to show tweets in time slices through the game's progression. I also enlarged the scope of the timeline to include 6 hours before the game and about 30 minutes post-game for context. Because my #NBAFinals dataset did not span this entire time range (game only), I eliminated it and focused on #Warriors vs #Cavaliers.

I also needed to fix a bug: d3.geomap has built-in zoom- and pan-on-click behavior that does not redraw appended data points scaled and transformed to the new map area. I had to modify the geomap source code to turn off these features. Eventually, I'd like to figure out how to redraw the data automatically upon zoom-in.

####Final thoughts
All in all, my intention was to communicate three main trends in the data: 
* where in the world people were watching the game (primarily the US, though it was unexpectedly popular in the Philippines, for example)
* how tweet frequency changed as the day/game progressed (trended upward and peaked at game's end), and
* the relative popularity of the two teams/hashtags. (#Warriors was far more popular, though at the time I didn't know about the popular alternate abbreviated hashtag #Cavs, so this study has its flaws)

My hope is that between the animated map and static histogram, those relationships are now better represented.

####Resources
I made heavy use of Mike Bostock's D3 documentation and examples generally, in particular:

http://d3-geomap.github.io/map/choropleth/world/

I obviously needed to read the twitter API docs:

https://dev.twitter.com/overview/documentation

I used this page for help figuring out the twitter API package for python:

https://rawgit.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition/master/ipynb/html/__Chapter%201%20-%20Mining%20Twitter%20(Full-Text%20Sampler).html

and a great blog post that really helped me with the python tweepy library that I finally chose after exploring 3 or 4 different twitter API libraries:

http://adilmoujahid.com/posts/2014/07/twitter-analytics/

The following page was helpful for adding textual svg elements:

https://www.dashingd3js.com/svg-text-element

I also read Scott Murray's book "Interactive Data Visualization" cover-to-cover to get a handle on D3.
