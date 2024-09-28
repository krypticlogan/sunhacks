from flask import Flask

app = Flask(__name__, template_folder='templateFiles',static_folder='static')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"