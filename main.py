# This is a sample Python script.
from flask import Flask, request, render_template, session, redirect, url_for
from database import Database
from objects import User
from authenticate import AuthenticationService
from Tweet_Extract import Tweet_manager

app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.secret_key = 'your_secret_key'

#Dependency Injection (DI) Pattern
db = Database("localhost", "root", "", "tweetdisarq")  # Replace with your actual database details
auth_service = AuthenticationService(db)
TwtMngr = Tweet_manager(db)


# login screen
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('Home.html')

@app.route('/login', methods=['POST'])
def login_check():
    #obtiene el userid y password de sus respectivas inputfields
    username = request.form['username']
    contrasena = request.form['password']
    user_master = auth_service.login(username, contrasena)
    #verifica si existe este usuario
    if user_master:
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
    # accede al variable global User
    user_dict = session.get('user')
    if user_dict:
        user = User(user_dict['name'], user_dict['nickname'])
    tweets_to_be_Shown = TwtMngr.get_Tweets()
    return render_template('DashBoard.html', data=tweets_to_be_Shown, Usr=user.nickname)

@app.route('/details/<int:tweet_id>', methods=['POST', 'GET'])
def details(tweet_id):
    if request.method == 'POST':
        reply_text = request.form['reply']
        insert_comment(reply_text, tweet_id)
        return redirect(url_for('details', tweet_id=tweet_id))

    data = TwtMngr.get_comments((tweet_id,))
    user_dict = session.get('user')
    if user_dict:
        user = User(user_dict['name'], user_dict['nickname'])
    selected = TwtMngr.get_selected_Tweet((tweet_id,))
    return render_template('details.html', threads=data, Usr=user.nickname, Tweet=tweet_id, Selctd = selected)

@app.route('/events', methods=['GET', 'POST'])
def events():
    # accede al variable global User
    user_dict = session.get('user')
    if user_dict:
        user = User(user_dict['name'], user_dict['nickname'])
    data = auth_service.get_events()
    return render_template('Event_Dash.html', data=data, Usr=user.nickname)

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
    TwtMngr.insert_comment(text, id, user.name)
    return "comment inserted successfully"

#Design pattern uses Mvc
def insert_tweet(text):
    #acceso al usuario
    user_dict = session.get('user')
    if user_dict:
        user = User(user_dict['name'], user_dict['nickname'])
    TwtMngr.insert_Tweet(text, user.name)
    return "Tweet inserted successfully"
if __name__ == '__main__':
    app.run()



