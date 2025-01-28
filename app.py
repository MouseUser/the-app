from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

def log_the_user_in(username):
    return

@app.route('/') # allows for different pages to be made
def hello():
    return(render_template("home.html"))

@app.route('/register', methods=['POST', "GET"])
def register():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            log_the_user_in(request.form['username'])
        else:
            error = "invalid username/password"
    return(render_template("register.html", error=error))