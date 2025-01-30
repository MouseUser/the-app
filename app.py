from flask import Flask, render_template, request, redirect
from markupsafe import escape

app = Flask(__name__)

def log_the_user_in(username):
    return

@app.route('/') # allows for different pages to be made
def hello():
    return(render_template("home.html"))

@app.route('/register', methods=['POST', "GET"])
def register():
    return(render_template("login.html"))