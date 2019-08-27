import os
from datetime import datetime
from flask import Flask, redirect

app = Flask(__name__)

messages = []

def add_messages(username, message):
    """ Add messages to message list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now,username, message))
    
def get_all_messages():
    """Gets all messages and seperates onto a newline"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main page wih instructions"""
    
    return "To send a message use /USERNAME/MESSAGE"

@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {} </h1>{} ".format(username, get_all_messages())
    
@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to chat page"""
    add_messages(username, message)
    
    return redirect("/" + username)
    
host = os.getenv('IP')
port = int(os.getenv('PORT'))

app.run(host, port, debug = True)