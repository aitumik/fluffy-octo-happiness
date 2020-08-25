from . import auth
from flask_login import login_user,logout_user
from flask import request,redirect,url_for,flash,render_template
from .forms import RegistrationForm,LoginForm
from app.models import User
from app import db

@auth.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u is not None and u.verify_password(form.password.data):
            login_user(u)
            return redirect(url_for('main.home'))
        return redirect(url_for('auth.login'))
    return render_template("auth/login.html",form=form)

@auth.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u is not None:
            return redirect(url_for('auth.register'))
        u = User(name=form.name.data,email=form.email.data,password=form.password.data)
        db.session.add(u)
        return redirect(url_for('auth.login'))
    return render_template("auth/register.html",form=form)