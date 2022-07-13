from flask import Flask
from flask import render_template

app = Flask(__name__)


# set FLASK_APP=main
# flask run --host=0.0.0.0

@app.route("/")
def hello_world():
    return "<p>Hello, World11111!</p>"


@app.route("/home/", methods=['GET', 'POST'])
def home():
    return "<p>home!</p>"


@app.route("/index/", methods=['GET', 'POST'])
def index():
    name = "Alice"
    return render_template('hello.html', name=name)
