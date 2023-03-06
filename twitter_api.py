import tweepy
import datetime




import numpy as np 
import pandas as pd 

# To consume Twitter's API
import tweepy
from tweepy import OAuthHandler 

"""
consumer_key = 'Sec3MvclRIx2RVlgu9l0SJX6D'
consumer_secret = 'ayoPNWtBm7fWpMBoK6EwRmegu3SW8Rw9mzJkottkv97quPe941'
access_token = '736550752760406018-so5CPJrEbJKb3c3Pq8va3VFr0yk4S0E'
access_token_secret = 'Cgr8tz0h6FTU7kxAjDzpHnjffNTHxWsBytXnu4Ihd1TFb'

class TwitterClient(object): 
    def __init__(self): 
        #Initialization method. 
        try: 
            # create OAuthHandler object 
            auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            # add hyper parameter 'proxy' if executing from behind proxy "proxy='http://172.22.218.218:8085'"
            self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            
        except tweepy.TweepError as e:
            print(f"Error: Tweeter Authentication Failed - \n{str(e)}")

    def get_tweets(self, query, maxTweets = 1000):
        #Function to fetch tweets. 
        # empty list to store parsed tweets 
        tweets = [] 
        sinceId = None
        max_id = -1
        tweetCount = 0
        tweetsPerQry = 100

        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = self.api.search(q=query, count=tweetsPerQry)
                    else:
                        new_tweets = self.api.search(q=query, count=tweetsPerQry,
                                                since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = self.api.search(q=query, count=tweetsPerQry,
                                                max_id=str(max_id - 1))
                    else:
                        new_tweets = self.api.search(q=query, count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    break

                for tweet in new_tweets:
                    parsed_tweet = {} 
                    parsed_tweet['tweets'] = tweet.text 

                    # appending parsed tweet to tweets list 
                    if tweet.retweet_count > 0: 
                        # if tweet has retweets, ensure that it is appended only once 
                        if parsed_tweet not in tweets: 
                            tweets.append(parsed_tweet) 
                    else: 
                        tweets.append(parsed_tweet) 
                        
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id

            except tweepy.TweepError as e:
                # Just exit if any error
                print("Tweepy error : " + str(e))
                break
        
        return pd.DataFrame(tweets)

twitter_client = TwitterClient()

# calling function to get tweets
tweets_df = twitter_client.get_tweets('ElonMusk', maxTweets=100000)
print(f'tweets_df Shape - {tweets_df.shape}')
tweets_df.head(10)
"""

######################################################

import pandas as pd

class API:
    def __init__(self):
        pass 
    def tweet_render(self):
        twt = pd.read_csv('./static/Files/Tweets.csv')
        return twt



"""

# Set up Twitter API credentials
# consumer_key =  "2b001c7b056c4b410d28f33cf"
# consumer_secret =  "eO5aNLJ4Eu51be719fd27f5f9db390cdc9c3d98f0e3"
# access_token =  "8980980401-M0iGY3MY55d3aae7037c0FkZoG4b11tdKZ8I1N"
# access_token_secret = "UzSRLYgbwNCmA3W9cxS00c64059dd8d31a080c56a0339LOL3ATU"

consumer_key = 'Sec3MvclRIx2RVlgu9l0SJX6D'
consumer_secret = 'ayoPNWtBm7fWpMBoK6EwRmegu3SW8Rw9mzJkottkv97quPe941'
access_token = '736550752760406018-so5CPJrEbJKb3c3Pq8va3VFr0yk4S0E'
access_token_secret = 'Cgr8tz0h6FTU7kxAjDzpHnjffNTHxWsBytXnu4Ihd1TFb'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Twitter screen name to extract conversation threads from
screen_name = "ylecun"

# February 2022 to March 2022 period
since_date = "2022-02-01"
until_date = "2022-03-31"

# Cursor to iterate through tweets
tweets = tweepy.Cursor(api.search_tweets, q='to:' + screen_name, tweet_mode='extended', since_id=0, since=since_date, until=until_date).items()
print(tweets)
# user_id = "ylecun"
# tweets = tweepy.Cursor(api.user_timeline, id=user_id, tweet_mode='extended',).items()

# Extract all conversation threads for each tweet

for tweet in tweets:
    # Get conversation thread for the tweet
    conversation = tweet.in_reply_to_status_id
    while conversation is not None:
        conv_tweet = api.get_status(conversation, tweet_mode='extended')
        print("Author: ", conv_tweet.author.name)
        print("Time: ", conv_tweet.created_at)
        print("Text: ", conv_tweet.full_text)
        conversation = conv_tweet.in_reply_to_status_id


tweets_dict = tweets.json() 

# Extract "data" value from dictionary
tweets_data = tweets_dict['data'] 

# Transform to pandas Dataframe
df = pd.json_normalize(tweets_data) 


"""