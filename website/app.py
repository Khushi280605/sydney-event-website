import os
from flask import Flask, render_template, json

app = Flask(__name__)

@app.route("/")
def home():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    events_path = os.path.join(base_dir, "events.json")
    with open(events_path) as f:
        events = json.load(f)
    return render_template("index.html", events=events)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
