from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-pattern", methods=["POST"])
def generatePatterns():
    updated_color1 = request.form.get('color1', 'red')
    updated_color2 = request.form.get('color2', 'green')
    updated_color3 = request.form.get('color3', 'blue')
    
    return render_template("results.html")

app.run(debug=True)