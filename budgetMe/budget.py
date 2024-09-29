from flask import Flask, render_template, jsonify, redirect, request
import requests
# from json impo
app = Flask(__name__, template_folder='templateFiles',static_folder='static')
access_token = None
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/breakdown")
def breakdown():
    print(access_token)
    if access_token:
        return render_template('myBreakdown.html')
    else:
        return render_template('login.html')

@app.route("/advice")
def advice():
    return render_template('financialAdvice.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/teller")
def teller():
    return render_template('teller.html')

@app.route('/save-token', methods=['POST'])
def save_token():
    data = request.json
    global access_token
    access_token = data.get('accessToken')

    if not access_token:
        return jsonify({'error': 'Access token missing'}), 400

    # Save token (for demonstration)
    print(f"Access Token: {access_token}")
    return render_template('myBreakdown.html')
# @app.route("/advice")
# def breakdown():
#     return render_template('advice.html')
