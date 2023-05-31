# This is a sample Python script.
from flask import Flask, request, render_template,jsonify
from datetime import datetime
from objects import Tweet, User
import mysql.connector
from datetime import datetime
import json

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tweetdisarq"  # Replace with your actual database name
)

@app.route('/')
def hello_world():
    #return 'Hello, World!  check out this tweet {}'.format(create_tweet())
    return render_template('Home.html')
@app.route('/create_tweet', methods=['POST'])
def create_tweet():
    return render_template('newTweet.html')

@app.route('/board', methods=['POST'])
def board():
    cursor = db.cursor()
    query = """
    SELECT t.fecha, t.text, u.nickname, t.hora
    FROM tweet AS t
    JOIN user AS u ON t.author = u.userid
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('DashBoard.html', data=data)
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


def insert_tweet(text):
    _datetime = datetime.now()
    # Convert date and time to strings
    cur_fecha = _datetime.strftime('%Y-%m-%d')
    cur_hora = _datetime.strftime('%H:%M:%S')
    cursor = db.cursor()
    query = """
    INSERT INTO tweet (fecha, hora, author, text)
    VALUES (%s, %s, %s, %s)
    """
    values = (cur_fecha, cur_hora, "ElOtoMotto", text)  # Replace with appropriate values for fecha, hora, and author
    cursor.execute(query, values)
    db.commit()
    return "Tweet inserted successfully"

@app.route('/submit', methods=['POST'])
def submit():
    tweet_text = request.form['tweet_text']
    insert_tweet(tweet_text)
    return "Tweet generated and inserted into the database successfully"

if __name__ == '__main__':
    app.run()



