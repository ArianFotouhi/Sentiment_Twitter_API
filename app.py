from sentiment import sentiment
# from twitter_api import API
from flask import Flask, request, url_for, redirect, send_file, render_template,jsonify
from twitter_api import Tweet_Extractor

import pytz
from datetime import datetime

utc = pytz.UTC



"""
# Receive tweets
tweets = api.tweet_render()
#separate tweets and replies
def tweet_reply_separate():
    pass
# find top 20 active users based on replies
def top_n_finder(n=20):
    pass
#sentiment analysis of a thread (tweet)
def sent_analysis_thread(text):
    analysis_res = text.Analysis()
    pass
#sentiment analysis of replies of a thread
"""

def sent_analysis_replies(twt):
    compound_rate = []
    for i,txt in enumerate(twt['text']):
            # print(txt)
        analyzed_txt = sentiment(txt)
        compound_rate.append(analyzed_txt.Analysis())
        if i ==25:
            break
    twt = twt.iloc[:26,:]
    twt['Sentiment'] = compound_rate
    twt=twt.drop(['sentiment'],axis=1)


    return twt





app = Flask(__name__)  

@app.route('/', methods = ['GET'])
def tweets_ylecun():

    # date_str = input("Enter a date (yyyy-mm-dd): ")
    date_str = '2023-2-22'
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    tweet_ext = Tweet_Extractor(until_date= date.replace(tzinfo=utc)) 
    df = tweet_ext.extractor()
    print(df)

    return render_template('tweets.html',dataframe=df.to_numpy())



if __name__=='__main__':

    app.run(host='127.0.0.1',port=8000,debug=True)


