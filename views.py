import datetime

from flask import Flask, redirect, render_template
from flask_login import login_user, login_required, logout_user, LoginManager

from data import db_session
from data.app import get_hot_products, get_prod_by_link, prods
from data.users import User
from forms.user_form import LoginForm, RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        return render_template('login.html',
                               message="Incorrect login or password",
                               form=form)
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Register',
                                   form=form,
                                   message="passwords must be same")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='register',
                                   form=form,
                                   message="User already exists")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init("db/database.db")
    app.run(debug=True)
