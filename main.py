# This is a sample Python script.
from flask import Flask, request, render_template,jsonify
from datetime import datetime
from objects import Tweet, User
from pymongo import MongoClient
import json

app = Flask(__name__)
#client = MongoClient('mongodb://localhost:27017/')
#db = client['your_database_name']

@app.route('/')
def hello_world():
    #return 'Hello, World!  check out this tweet {}'.format(create_tweet())
    return render_template('Home.html')


@app.route('/create_tweet', methods=['POST'])
def create_tweet():
    # Get the text of the tweet from the request data
    text = "Hola, como estan este es un tweet"##request.form['text']

    # Set the default author and timestamp
    author = "testAuthor"
    timestamp = datetime.now()

    # Create a new instance of the Tweet class with the provided text, author, and timestamp
    tweet = Tweet(text, author, timestamp)

    # Do something with the new tweet instance (e.g. store it in a database)
    # ...

    return render_template('newTweet.html')


@app.route('/board', methods=['POST'])
def board():
    tweets = load_tweets_from_json()
    return render_template('DashBoard.html', tweets=tweets)

@app.route('/details', methods=['POST'])
def details():
    thread = load_tweets_from_json()
    tweet = {
        "username": "michael_wilson",
        "content": "Finally got around to watching that movie everyone's been raving about. It definitely lived up to the hype!",
        "timestamp": "2023-05-25 14:20:12"
    }
    return render_template('details.html', tweet=tweet, threads=thread)
def load_tweets_from_json():
    with open('tweets.json') as file:
        tweets = json.load(file)
    return tweets


if __name__ == '__main__':
    app.run()



