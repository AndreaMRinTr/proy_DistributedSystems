class Tweet:
    def __init__(self, text, author, timestamp, hour, id):
        self.text = text
        self.author = author
        self.timestamp = timestamp
        self.hour = hour
        self.comments = ()
        self.id = id

class User:
    def __init__(self, userid, nickname):
        self.name = userid
        self.nickname = nickname
        self.tweets = []
        self.replies = []
        self.password =""
class Event:
    def __init__(self, Type, author, fecha, hora, text):
        self.eType = Type
        self.author = author
        self.fecha = fecha
        self.hora = hora
        self.desc = text