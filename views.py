from flask import render_template
from flask import Flask
from data.app import get_hot_products


app = Flask(__name__)

@app.route('/')
def base():
    context = {'products': get_hot_products()}
    products = context
    return render_template('index.html', **products)

@app.route('/store')
def store():
    return render_template('store.html')

def main():
    app.run(debug=True)