from flask import Flask, render_template, request, jsonify

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
    
    colors = {
        "color 1": color1,
        "color 2": color2,
        "color 3": color3
    }
    
    return jsonify(colors=colors)

app.run(debug=True)