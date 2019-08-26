import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello</h1>"
    
    
host = os.getenv('IP')
port = int(os.getenv('PORT'))
app.run(host, port, debug = True)