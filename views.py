from flask import Flask
from flask import render_template

from data.app import get_hot_products, get_catalog

app = Flask(__name__)


@app.route('/')
def base():
    prods, big = get_hot_products()
    context = {'products': prods, 'big_info': big}
    return render_template('index.html', **context)


@app.route('/store')
def store():
    catalog = get_catalog()
    filter_data = (min([x.get('price') for x in catalog]), max([x.get('price') for x in catalog]))
    context = {'catalog': catalog, 'filter_data': filter_data}
    # print(context)
    return render_template('store.html', **context)


def main():
    app.run(debug=True)
