import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Main page wih instructions"""
    
    return "To send a message use /USERNAME/MESSAGE"

@app.route('/<username>')
def user(username):
    return "Hi " + username
    
@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)   
    
host = os.getenv('IP')
port = int(os.getenv('PORT'))

app.run(host, port, debug = True)