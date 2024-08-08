from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-patterns")
def generatePatterns():
    return render_template("results")

app.run(debug=True)