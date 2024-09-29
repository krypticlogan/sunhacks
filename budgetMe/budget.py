from flask import Flask, render_template, jsonify, redirect, request, url_for
import requests
from time import sleep
import json
import budgetMe.data
# from json impo

def call(route, auth):
    r = requests.get(route, auth=(auth, '')).json()
    if isinstance(r, list):
        return r[0]
    return r

app = Flask(__name__, template_folder='templateFiles',static_folder='static')
access_token = None
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/breakdown")
def breakdown():
    print(access_token)
    if not access_token:
        print("no access token")
        return redirect('/login')
    

    print(access_token)

    # requests.post('https://api.teller.io/accounts', headers=)
    # response = requests.get('https://api.teller.io/accounts', auth=(access_token, ''))
    data = call('https://api.teller.io/accounts', auth=access_token)
    # dict(response)


    # print(response)
    # response = response.json()
    # data = response[0]
    print(data.keys())
    # print(type(data))
    currency = data['currency']
    # enrollment_id = 
    # name = data['name']
    institution = data['institution']['name']
    # accounts = data['institution']['name']

    links = data['links']

    balances = links['balances']
    

    

    transactions = links['transactions']


    # print(transactions)
    transactions = call(transactions, auth=access_token)
    balances = call(balances, auth=access_token)

    print(balances)
    currentAccBal = balances['available']
    print(currentAccBal)

    print(transactions, transactions.keys())
    accounts = []
    

    return render_template('breakdown.html', balance=currentAccBal, accounts=accounts, transactions=transactions)

@app.route("/advice")
def advice():
    return render_template('advice.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    global access_token
    # if access_token:
    
    if request.method == 'POST':
        print('no token')
        data = request.json
        access_token = data.get('accessToken')

        # if not access_token:
        #     return jsonify({'error': 'Access token missing'}), 400
        

        # Save token (for demonstration)
        print(f"Access Token: {access_token}")
        return redirect('/breakdown')
        
    return render_template('login.html')

# @app.route("/teller")
# def teller():
#     return render_template('teller.html')

@app.route('/save-token', methods=['POST'])
def save_token():
    

    # sleep(1.5)
    return redirect('/breakdown')
# @app.route("/advice")
# def breakdown():
#     return render_template('advice.html')
