from flask import Flask
from flask import render_template

from data.app import get_hot_products

app = Flask(__name__)


@app.route('/')
def base():
    prods, big = get_hot_products()
    context = {'products': prods, 'big_info': big}
    return render_template('index.html', **context)


@app.route('/store')
def store():
    return render_template('store.html')


def main():
    app.run(debug=True)
