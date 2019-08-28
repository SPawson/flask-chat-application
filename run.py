import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)#Creating an instance of the Flask class
app.secret_key = os.getenv("SECRET", "randomstring123") # uses secret key for encryption of session vars


messages = [] #creates empty list

def add_message(username, message):
    """ Add messages to message list"""
    now = datetime.now().strftime("%H:%M:%S")#gets the current time
    
    # Creates key value pair dictionary
    messages.append({"timestamp": now, "from": username, "message": message}) #adds time,name and message as an item into the message list


@app.route('/', methods = ["GET", "POST"]) # defines access methods that can be used
def index():
    """Main page wih instructions"""
    
    if request.method == "POST":
        session["username"] = request.form["username"] #Stores session variable username 
        
    if "username" in session: #Checks to see if session variable exists
        return redirect(url_for("user", username= session["username"])) #redirects to username view using username as route
    
    return render_template("index.html") #Renders html page template

@app.route('/chat/<username>', methods = ["GET", "POST"])
def user(username):
    """Add & display chat messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        
        return redirect(url_for("user", username= session["username"]))
        
    return render_template("chat.html", username = username,
    chat_messages = messages)
    #Displays all messages in list after heading
    
host = os.getenv('IP', '0.0.0.0')
port = int(os.getenv('PORT', '5000')) #secondary param will act as default
#no need to setup in config file for heroku

app.run(host, port, debug = False)