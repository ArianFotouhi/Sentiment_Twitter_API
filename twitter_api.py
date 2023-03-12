import tweepy
import datetime

import snscrape.modules.twitter as sntwitter
import pandas as pd
import pytz
from datetime import datetime

utc = pytz.UTC



class Tweet_Extractor:
    def __init__(self, user='elonmusk',since_date = datetime(2023, 2, 1).replace(tzinfo=utc), until_date = datetime.today().replace(tzinfo=utc)):
        self.user = user
        self.since_date = since_date
        self.until_date = until_date

    
    def extractor(self):

        # set search query
        search_query = f'from:{self.user}'

        # iterate through search results and extract replies
        replies_list = []
        # for tweet in sntwitter.TwitterSearchScraper(f'from:{self.user} since:{self.since_date} until:{self.until_date}').get_items():
    
        for tweet in sntwitter.TwitterSearchScraper(search_query +  ' since:' + self.since_date.strftime('%Y-%m-%d')+  ' until:' + self.until_date.strftime('%Y-%m-%d') ).get_items():
            replies_list.append([tweet.id, tweet.content, tweet.date, tweet.user.username])

        # convert replies to dataframe
        replies_df = pd.DataFrame(replies_list, columns=['id', 'text', 'date', 'username'])
        return replies_df
   