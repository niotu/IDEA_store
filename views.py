from flask import render_template
from flask import Flask
from data.app import


app = Flask(__name__)

@app.route('/')
def base():
    context = {}
    return render_template('index.html', **context)

@app.route('/store')
def store():
    return render_template('store.html')

def main():
    app.run()