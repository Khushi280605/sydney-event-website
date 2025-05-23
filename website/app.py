from flask import Flask, render_template, json

app = Flask(__name__)

@app.route("/")
def home():
    with open("events.json") as f:
        events = json.load(f)
    return render_template("index.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)
