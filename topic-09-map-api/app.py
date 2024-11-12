import json
from flask import Flask, render_template

app = Flask(__name__)
private = json.load(open("private.json","r"))

@app.route("/")
def get_index():
    return render_template("index.html",api_key=private["API_KEY"], markers = [
    {
        "position": "37.4220656,-122.0840897",
        "title":"Mountain View, CA"
    },
    {
        "position": "47.648994,-122.3503845",
        "title":"Seattle, WA"
    },
    {
        "position": "49.648994,-132.3503845",
        "title":"Somewhere, WA"
    }
    ])

@app.route("/map")
def get_map():
    return render_template("map.html")
    
@app.route("/example")
def get_example():
    return render_template("example.html")
    
if __name__ == "__main__":
    app.run(debug = True)