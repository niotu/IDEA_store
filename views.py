from flask import render_template
from flask import Flask


app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/store')
def store():
    return render_template('store.html')

def main():
    app.run()