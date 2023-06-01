# app.py
from flask import Flask, request, render_template, session, redirect, url_for
from database import Database
from authenticate import AuthenticationService
from objects import User, Tweet

app = Flask(__name__)
app.secret_key = 'your_secret_key'
database = Database("localhost", "root", "", "tweetdisarq")  # Replace with your actual database details
auth_service = AuthenticationService(database)

@app.route('/login', methods=['POST'])
def login_check():
    username = request.form['username']
    password = request.form['password']

    user = auth_service.login(username, password)

    if user:
        session['user'] = user.__dict__
        return redirect('/board')
    else:
        return "error"
