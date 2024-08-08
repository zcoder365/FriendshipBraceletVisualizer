from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-pattern", methods=["POST"])
def generatePatterns():
    color1 = request.form["color1"]
    color2 = request.form["color2"]
    color3 = request.form["color3"]
    
    print(f"{color1}\n{color2}\n{color3}")
    
    return render_template("results.html")

app.run(debug=True)