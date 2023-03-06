from sentiment import sentiment
from twitter_api import API
from flask import Flask, request, url_for, redirect, send_file, render_template,jsonify

#sample of using
# text = sentiment('Worst movie in history!')

api = API()
twt = api.tweet_render()
for i,txt in enumerate(twt):
    print(txt)
    analyzed_txt = sentiment(txt['text'])
    print(analyzed_txt.Analysis())
    if i ==20:
        break


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
def sent_analysis_replies(text):
    analysis_res = text.Analysis()
    pass
"""



"""
@app.route('/accounts', methods = ['GET'])
def accounts():
    # token = request.args.get('token')
    # account_name = token2username(token)
    
    # blc=render_chain(account_name)

    return render_template('blk.html')
"""

app = Flask(__name__)   
@app.route('/tweets/ylecun', methods = ['GET'])
def tweets_ylecun():


    return render_template('tweets.html')


"""
@app.route('/tweets/elonmusk', methods = ['GET'])
def tweets_elonmusk():
    # token = request.args.get('token')
    # account_name = token2username(token)
    
    # blc=render_chain(account_name)

    return render_template('blk.html',chain =blc, length=len(blc),token=token)


@app.route('/tweets/cathiedwood', methods = ['GET'])
def tweets_cathiedwood():
    # token = request.args.get('token')
    # account_name = token2username(token)
    
    # blc=render_chain(account_name)

    return render_template('blk.html',chain =blc, length=len(blc),token=token)




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
    # token = request.args.get('token')
    # account_name = token2username(token)
    
    # blc=render_chain(account_name)

    return render_template('blk.html',chain =blc, length=len(blc),token=token)

@app.route('/sentiment/elonmusk', methods = ['GET'])
def tweets_elonmusk():
    # token = request.args.get('token')
    # account_name = token2username(token)
    
    # blc=render_chain(account_name)

    return render_template('blk.html',chain =blc, length=len(blc),token=token)


@app.route('/sentiment/cathiedwood', methods = ['GET'])
def tweets_cathiedwood():
    # token = request.args.get('token')
    # account_name = token2username(token)
    
    # blc=render_chain(account_name)

    return render_template('blk.html',chain =blc, length=len(blc),token=token)
"""