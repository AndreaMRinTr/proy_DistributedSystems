class Tweet:
    def __init__(self, text, author, timestamp):
        self.text = text
        self.author = author
        self.timestamp = timestamp
        self.comments = []

class User:
    def __init__(self, name, handle):
        self.name = name
        self.handle = handle
        self.tweets = []
        self.replies = []
        self.password =""

    def create_tweet(self, text, timestamp):
        tweet = Tweet(text, self, timestamp)
        self.tweets.append(tweet)
        return tweet

    def reply_to_tweet(self, tweet, text, timestamp):
        reply = Tweet(text, self, timestamp)
        tweet.replies.append(reply)
        self.replies.append(reply)
        return reply

class Thread:
    def __init__(self, original_tweet):
        self.original_tweet = original_tweet
        self.replies = []

    def add_reply(self, reply):
        self.replies.append(reply)