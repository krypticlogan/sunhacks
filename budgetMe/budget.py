from flask import Flask, render_template, redirect, request
import requests
app = Flask(__name__, template_folder='templateFiles',static_folder='static')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/breakdown")
def breakdown():
    return render_template('myBreakdown.html')

@app.route("/advice")
def advice():
    return render_template('financialAdvice.html')

@app.route("/login")
def login():
    return render_template('login.html')

