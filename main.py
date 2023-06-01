# This is a sample Python script.
from flask import Flask, request, render_template, session, redirect, url_for
import mysql.connector
from datetime import datetime
import json
from objects import User


app = Flask(__name__)
app.secret_key = 'your_secret_key'
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tweetdisarq"  # Replace with your actual database name
)
cursor = db.cursor()

# login screen
@app.route('/', methods=['GET'])
def hello_world():
    #return 'Hello, World!  check out this tweet {}'.format(create_tweet())
    return render_template('Home.html')

@app.route('/login', methods=['POST'])
def login_check():
    #obtiene el userid y password de sus respectivas inputfields
    username = request.form['username']
    contrasena = request.form['password']
    #hash = password.hash_password(contrasena)

    #establece el query que sera llevado acabo y regresa los resultados
    # los guarda en user_info
    query = "SELECT * FROM user WHERE userid= %s AND passw = %s"
    cursor.execute(query, (username, contrasena))
    user_info = cursor.fetchone()

    #verifica si existe este usuario
    if user_info:
        user_master = User(user_info[0], user_info[1])
        user_master.password = user_info[2]
        session['user'] = user_master.__dict__
        return redirect('/board')
    else:
        return "error"


#pagina donde se crean tweets nuevos
@app.route('/create_tweet', methods=['POST'])
def create_tweet():
    # accede al variable global User
    user_dict = session.get('user')
    if user_dict:
        user = User(user_dict['name'], user_dict['nickname'])
    return render_template('newTweet.html', Usr=user.nickname)


#Dashboard del usuario
@app.route('/board', methods=['GET', 'POST'])
def board():
    query = """
    SELECT t.fecha, t.text, u.nickname, t.hora,t.id
    FROM tweet AS t
    JOIN user AS u ON t.author = u.userid
    """
    cursor.execute(query)
    data = cursor.fetchall()

    #accede al variable global User
    user_dict = session.get('user')
    if user_dict:
        user = User(user_dict['name'], user_dict['nickname'])

    return render_template('DashBoard.html', data=data, Usr=user.nickname)

#this is temporary but it will display los comentarios
@app.route('/details/<int:tweet_id>', methods=['POST', 'GET'])
def details(tweet_id):
    if request.method == 'POST':

        reply_text = request.form['reply']

        insert_comment(reply_text, tweet_id)

        return redirect(url_for('details', tweet_id=tweet_id))
    query = """
   SELECT t.fecha, t.text, u.nickname, t.hora
   FROM comment AS t
   JOIN user AS u ON t.userid = u.userid
   WHERE   t.id_tweet = %s
   """
    cursor.execute(query, (tweet_id,))
    data = cursor.fetchall()

    user_dict = session.get('user')
    if user_dict:
        user = User(user_dict['name'], user_dict['nickname'])
    selected = getSingleTweet(tweet_id)
    return render_template('details.html', threads=data, Usr=user.nickname, Tweet=tweet_id, Selctd = selected)

def getSingleTweet(tweet_id):
    query = """SELECT t.fecha, t.text, u.nickname, t.hora,t.id
    FROM tweet AS t
    JOIN user AS u ON t.author = u.userid
    WHERE   t.id = %s
    """
    cursor.execute(query, (tweet_id,))
    data = cursor.fetchone()
    return data
#ya no se necesita

#crea un tweet, pero hay que tener acceso al usuario primero antes de insertarlo en la DB
def insert_tweet(text):
    #acceso al usuario
    user_dict = session.get('user')
    if user_dict:
        user = User(user_dict['name'], user_dict['nickname'])

    _datetime = datetime.now()
    # Convert date and time to strings
    cur_fecha = _datetime.strftime('%d/%m/%Y')
    cur_hora = _datetime.strftime('%H:%M:%S')
    cursor = db.cursor()

    query = """
    INSERT INTO tweet (fecha, hora, author, text)
    VALUES (%s, %s, %s, %s)
    """
    values = (cur_fecha, cur_hora,user.name, text)  # Replace with appropriate values for fecha, hora, and author
    cursor.execute(query, values)
    db.commit()
    return "Tweet inserted successfully"

@app.route('/submit', methods=['POST'])
def submit():
    tweet_text = request.form['tweet_text']
    insert_tweet(tweet_text)
    return redirect('/board')

def insert_comment(text,id):
    # acceso al usuario
    user_dict = session.get('user')
    if user_dict:
        user = User(user_dict['name'], user_dict['nickname'])
    _datetime = datetime.now()
    # Convert date and time to strings
    cur_fecha = _datetime.strftime('%d/%m/%Y')
    cur_hora = _datetime.strftime('%H:%M:%S')
    cursor = db.cursor()

    query = """
        INSERT INTO comment (id_tweet,fecha,hora,userid,text)
        VALUES (%s, %s, %s, %s, %s)
        """
    values = (id, cur_fecha, cur_hora, user.name, text)  # Replace with appropriate values for fecha, hora, and author
    cursor.execute(query, values)
    db.commit()
    return "comment inserted successfully"

if __name__ == '__main__':
    app.run()



