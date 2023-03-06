from sentiment import sentiment
from twitter_api import API
from flask import Flask, request, url_for, redirect, send_file, render_template,jsonify

sent = sentiment('Worst movie in history!')
api = API()

print(sent.Analysis())
print(api.tweet_render())

