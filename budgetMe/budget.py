from flask import Flask, render_template, redirect, request
import requests
app = Flask(__name__, template_folder='templateFiles',static_folder='static')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/breakdown")
def breakdown():
    return render_template('analysis.html')

# @app.route("/advice")
# def breakdown():
#     return render_template('advice.html')
