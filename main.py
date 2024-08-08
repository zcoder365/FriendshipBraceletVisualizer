from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-pattern", methods=["POST"])
def generatePatterns():
    color1 = "red"
    color2 = "blue"
    color3 = "white"
    
    print(f"{color1}\n{color2}\n{color3}")
    
    colors = {
        "color 1": color1,
        "color 2": color2,
        "color 3": color3
    }
    
    return jsonify(colors=colors)

app.run(debug=True)