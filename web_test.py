import os
from flask import Flask
app = Flask(__name__)

@app.route("/")

def main():
    return "welcome"

@app.route('/how are you')
def hello():
    return ' im good and u ?'

if __name__ -- "__main__":
    app.run(host="0.0.0.0",port=8086)
