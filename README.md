## NBATweets
Final project for Udacity Data Visualization Course: collect tweets during the NBA finals and map them using D3.

I created a pipeline that allows me to:
- catch tweets from the twitter streaming API matching a given search query
- filter the tweets for those containing GPS coordinate information
- output the coordinate information in csv to be read in D3
- interactively visualize tweets on a global map using D3/JS/HTML

As an example, I collected tweets matching 3 queries during the last game of the 2015 NBA finals on June 16th. The queries were: 'Warriors', 'Cavaliers', and 'NBAfinals'. The visualization includes toggle buttons to select each search term, and when pressed, you can watch the tweets appear on the map chronologically as the game proceeded.

