from sentiment import sentiment
from twitter_api import API
from flask import Flask, request, url_for, redirect, send_file, render_template,jsonify

#sample of using
# text = sentiment('Worst movie in history!')

api = API()
twt = api.tweet_render()
# for i,txt in enumerate(twt['text']):
#     print(txt)
#     analyzed_txt = sentiment(txt)
#     print(analyzed_txt.Analysis())
#     if i ==20:
#         break


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




"""
@app.route('/accounts', methods = ['GET'])
def accounts():
    # token = request.args.get('token')
    # account_name = token2username(token)
    
    # blc=render_chain(account_name)

    return render_template('blk.html')
"""

app = Flask(__name__)  
api = API()

@app.route('/tweets/ylecun', methods = ['GET'])
def tweets_ylecun():

    
    twt = api.tweet_render(id='ylecun')
    twt = sent_analysis_replies(twt)
    
    return render_template('tweets.html',dataframe=twt.to_numpy())



if __name__=='__main__':

    app.run(host='127.0.0.1',port=8000,debug=True)

"""
@app.route('/tweets/elonmusk', methods = ['GET'])
def tweets_elonmusk():
    
    twt = api.tweet_render(id='elonmusk')
    twt = sent_analysis_replies(twt)
    
    return render_template('tweets.html',dataframe=twt.to_numpy())


@app.route('/tweets/cathiedwood', methods = ['GET'])
def tweets_cathiedwood():
    
    twt = api.tweet_render(id='elonmusk')
    twt = sent_analysis_replies(twt)
    
    return render_template('tweets.html',dataframe=twt.to_numpy())



@app.route('/audience/ylecun', methods = ['GET'])
def tweets_ylecun():
    # token = request.args.get('token')
    # account_name = token2username(token)
    
    # blc=render_chain(account_name)

    return render_template('blk.html',chain =blc, length=len(blc),token=token)

@app.route('/audience/elonmusk', methods = ['GET'])
def tweets_elonmusk():
    # token = request.args.get('token')
    # account_name = token2username(token)
    
    # blc=render_chain(account_name)

    return render_template('blk.html',chain =blc, length=len(blc),token=token)


@app.route('/audience/cathiedwood', methods = ['GET'])
def tweets_cathiedwood():
    # token = request.args.get('token')
    # account_name = token2username(token)
    
    # blc=render_chain(account_name)

    return render_template('blk.html',chain =blc, length=len(blc),token=token)



@app.route('/sentiment/ylecun', methods = ['GET'])
def tweets_ylecun():

   twt = api.tweet_render(id='ylecun')
    twt = sent_analysis_replies(twt)
    
    return render_template('sent_tweets.html',dataframe=twt.to_numpy())

@app.route('/sentiment/elonmusk', methods = ['GET'])
def tweets_elonmusk():

    twt = api.tweet_render(id='elonmusk')
    twt = sent_analysis_replies(twt)
    
    return render_template('tweets_sent.html',dataframe=twt.to_numpy())


@app.route('/sentiment/cathiedwood', methods = ['GET'])
def tweets_cathiedwood():

    twt = api.tweet_render(id='cathiedwood')
    twt = sent_analysis_replies(twt)
    
    return render_template('tweets_sent.html',dataframe=twt.to_numpy())
"""

