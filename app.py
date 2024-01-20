from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world! This webapp is now deployed on Jenkins pipeline.'
