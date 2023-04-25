import datetime

from flask import Flask, redirect, render_template
from flask_login import login_user, login_required, logout_user, LoginManager, current_user

from data import db_session
from data.app import get_hot_products, get_prod_by_link, prods
from data.users import User
from data.amount import Amount
from forms.user_form import LoginForm, RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)

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
    amount = Amount()
    context = {"title": title, 'item': item, 'images': images, 'amount': amount}
    return render_template('product.html', **context)


@app.route('/store/add_to_cart/<link>')
def add_to_cart(link):
    try:
        link, amo = link.split(';')
        amo = int(amo)
        item = get_prod_by_link(link)
        if item.amount >= amo:
            item.amount -= amo
            item.save_amount()
            current_user.cart += f"{item.link}:{amo};"
            current_user.save_cart()
        return redirect(f'/store/{item.link}')
    except AttributeError:
        return redirect('/login')


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
            surname=form.surname.data,
            address=form.address.data,
            email=form.email.data,
            cart=';'
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/personal')
def personal():
    c = current_user.cart.split(';')
    cart = []
    total = 0
    if c:
        for i in c:
            if i != '':
                link, amount = i.split(":")
                item = get_prod_by_link(link)
                total += item.price * int(amount)
                items = {
                    "item": item,
                    "amount": amount
                }
                flag = False
                for lst in cart:
                    if lst["item"] == item:
                        flag = True
                        lst["amount"] = str(int(lst["amount"]) + 1)
                if not flag:
                    cart.append(items)
    user = {'name': current_user.name, 'surname': current_user.surname, 'address': current_user.address,
            'cart': cart, "total": str(total)}
    context = {'title': 'Personal', 'user': user}
    return render_template('personal.html', **context)


@app.route('/clear_cart')
@login_required
def clear_user_cart():
    current_user.clear_cart()
    return redirect("/personal")


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
    app.run(host="192.168.3.93", port=5000, debug=True)
