from flask import Flask, render_template

app = Flask(__name__, template_folder='templateFiles',static_folder='static')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/analysis")
def breakdown():
    return render_template('analysis.html')

