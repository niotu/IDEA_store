from flask import Flask
from flask import render_template

from data.app import get_hot_products, get_prod_by_link, prods

app = Flask(__name__)


@app.route('/')
def base():
    prods, big = get_hot_products()
    context = {'title': 'IDEA', 'products': prods, 'big_info': big}
    return render_template('index.html', **context)


@app.route('/store')
def store():
    catalog = prods
    filter_data = (min([x.price for x in catalog]), max([x.price for x in catalog]))
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


@app.route('/login')
def login():
    context = {"title": "Login"}
    return render_template('login.html', **context)


@app.route('/register')
def register():
    context = {"title": "Register"}
    return render_template('register.html', **context)



def main():
    app.run(debug=True)
