from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user
from flask_login.utils import logout_user

from market import app, db
from market.forms import (LoginForm, PurchaseItemForm, RegisterForm,
                          SaleItemForm)
from market.models import Item, User


# routes / views
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return "<h1> About Page</h1>"


@app.route('/market', methods=["GET", "POST"])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    selling_form = SaleItemForm()
    if request.method == "POST":
        # Purchase Item
        purchased_item = request.form.get('purchased_item')
        p_item_obj = Item.query.filter_by(name=purchased_item).first()
        if p_item_obj:
            if current_user.can_purchase(p_item_obj):
                p_item_obj.buy(current_user)
                flash(f"Congratulations! You have purchased {p_item_obj.name} \
                    for {p_item_obj.price}$",
                      category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase \
                    {p_item_obj.name}!",
                      category='danger')

        # Sale Item
        sold_item = request.form.get('sold_item')
        s_item_obj = Item.query.filter_by(name=sold_item).first()
        if s_item_obj:
            if current_user.can_sale(s_item_obj):
                s_item_obj.sell(current_user)
                flash(f"Congratulations! You have sold {s_item_obj.name} back \
                        to the Market", category='success')
            else:
                flash(f"Something went wrong with selling {s_item_obj.name}",
                      category='danger')

        return redirect(url_for('market_page'))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template(
            'market.html',
            items=items,
            purchase_form=purchase_form,
            owned_items=owned_items,
            selling_form=selling_form,
        )


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now loged in\
            as {user_to_create.username}", category='success')

        return redirect(url_for('market_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error with creating a user: {err_msg}",
                  category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data):
            login_user(attempted_user)
            flash(
                f"Success! You have logged in as: {attempted_user.username}",
                category='success')
            return redirect(url_for('market_page'))
        else:
            flash("Username and Password not matched! Please try again",
                  category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logout", category='info')
    return redirect(url_for('home_page'))
