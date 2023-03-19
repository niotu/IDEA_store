from flask import Flask
from flask import render_template

from data.app import get_hot_products, get_catalog, get_prod_by_link

app = Flask(__name__)


@app.route('/')
def base():
    prods, big = get_hot_products()
    context = {'title': 'IDEA', 'products': prods, 'big_info': big}
    return render_template('index.html', **context)


@app.route('/store')
def store():
    catalog = get_catalog()
    filter_data = (min([x.get('price') for x in catalog]), max([x.get('price') for x in catalog]))
    context = {'title': 'IDEA - catalog', 'catalog': catalog, 'filter_data': filter_data}
    # print(context)
    return render_template('store.html', **context)

@app.route('/store/<link>')
def product(link):
    item = get_prod_by_link(link)
    title = item.get_title()
    images = item.get_other_images()
    context = {"title": title, 'item': item, 'images': images}
    return render_template('product.html', **context)

def main():
    app.run(debug=True)
