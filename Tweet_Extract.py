from objects import Tweet
from datetime import datetime

class Tweet_manager:
    def __init__(self, database):
        self.db = database

    def get_Tweets(self):
        tweets_to_be_Shown = []
        query = """
            SELECT t.fecha, t.text, u.nickname, t.hora,t.id
            FROM tweet AS t
            JOIN user AS u ON t.author = u.userid
            ORDER BY fecha DESC, hora DESC
            LIMIT 10;
            """
        data = self.db.execute_query(query)
        # Data Access Object (DAO) Pattern:
        print(data)
        for item in data:
            twt = Tweet(item[1], item[2], item[0], item[3], item[4])
            print("Author:", twt.author)
            print("Text:", twt.text)
            print("Timestamp:", twt.timestamp)
            print("Hour:", twt.hour)
            print("----------")
            # la siguiente funcion se encarga de conseguir todos los commentarios
            query_2 = """
                       SELECT c.fecha, c.text, u.nickname, c.hora
                       FROM comment AS c
                       JOIN user AS u ON c.userid = u.userid
                       WHERE   c.id_tweet = %s
                       ORDER BY fecha DESC, hora DESC;
                       """
            reply = self.db.execute_query(query_2, (item[4],))
            twt.comments = reply
            tweets_to_be_Shown.append(twt)
        return tweets_to_be_Shown
    def get_comments(self, tweet_id):
        query = """
           SELECT t.fecha, t.text, u.nickname, t.hora
           FROM comment AS t
           JOIN user AS u ON t.userid = u.userid
           WHERE   t.id_tweet = %s
           """
        data = self.db.execute_query(query, tweet_id)
        return data
    def get_selected_Tweet(self,tweet_id):
        query = """SELECT t.fecha, t.text, u.nickname, t.hora,t.id
            FROM tweet AS t
            JOIN user AS u ON t.author = u.userid
            WHERE   t.id = %s
            """
        # cursor.execute(query, (tweet_id,))
        # data = cursor.fetchone()
        data = self.db.execute_queryone(query, tweet_id)
        return data
    def insert_Tweet(self, text, name):
        _datetime = datetime.now()
        # Convert date and time to strings
        cur_fecha = _datetime.strftime('%d/%m/%Y')
        cur_hora = _datetime.strftime('%H:%M:%S')
        query = """
                INSERT INTO tweet (fecha,hora,author,text)
                VALUES (%s, %s, %s, %s)
                """
        values = (cur_fecha, cur_hora, name, text)
        self.db.execute_insert(query, values)

    def insert_comment(self,text, tweet_id,name):
        _datetime = datetime.now()
        # Convert date and time to strings
        cur_fecha = _datetime.strftime('%d/%m/%Y')
        cur_hora = _datetime.strftime('%H:%M:%S')
        query = """
                INSERT INTO comment (id_tweet,fecha,hora,userid,text)
                VALUES (%s, %s, %s, %s, %s)
                """
        values = (tweet_id, cur_fecha, cur_hora, name, text)
        self.db.execute_insert(query,values)