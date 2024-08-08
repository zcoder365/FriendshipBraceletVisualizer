from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-pattern", methods=["POST"])
def generatePatterns():
    return render_template("results.html")

app.run(debug=True)