# This is a sample Python script.
from flask import Flask, request, render_template
from datetime import datetime
from objects import Tweet
app = Flask(__name__)


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
    return render_template('DashBoard.html')

if __name__ == '__main__':
    app.run()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



