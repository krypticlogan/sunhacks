import requests, os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('TELLER_API_ID')

# print(API_KEY)
url = "https://api.teller.io/accounts"

cert_file = "C:\\Users\\krypt\\Downloads\\teller\\certificate.pem"
key_file = "C:\\Users\\krypt\\Downloads\\teller\\private_key.pem"
headers = {
    'Authorization': f'Basic {API_KEY}:',
}

response = requests.get(url, headers=headers,cert=(cert_file,key_file))

if response.status_code == 200:
    # Printing the JSON response with account information
    print(response.json())
else:
    # Printing the error message
    print(f"Error: {response.status_code}, {response.text}")