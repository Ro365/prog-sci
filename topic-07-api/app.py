from flask import Flask
import datetime, time

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def get_hello():
    return "<p>Hello, World!</p>"

@app.route("/goodbye")
def get_goodbye():
    return "<p>Goodbye. See you later!</p>"

@app.route("/greeting")
@app.route("/greeting/<n>")
def get_greeting(n="0"):
    greeting = "It is "
    for i in range(0,int(n)):
        greeting = greeting + "really "
    greeting = greeting + "nice to see you!"
    return "<p>"+greeting+"</p>"

def current_iso_time():
    return datetime.datetime.fromtimestamp(time.time(),datetime.UTC).isoformat()

@app.route("/time")
def get_time():
    return "<p>"+current_iso_time()+"</p>"


@app.route("/api/time")
def get_api_time():
    date = datetime.datetime.fromtimestamp(time.time(),datetime.UTC)

    return {
        "year":date.year,
        "month":date.month,
        "day":date.day,
        "hour":date.hour,
        "minute":date.minute,
        "second":date.second,
        "timezone":"UTC"
    }