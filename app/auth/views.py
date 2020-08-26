from . import auth
from flask_login import login_user,logout_user,login_required
from flask import request,redirect,url_for,flash,render_template
from .forms import RegistrationForm,LoginForm
from app.models import User
from app import db

@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get("email",None)
        email = request.form.get("email",None)
        password = request.form.get("pass",None)
        if email is None or password is None:
            flash("There is an error in your fields")
            return redirect(url_for('auth.login'))
        u = User.query.filter_by(email=email).first()
        if u is not None and u.verify_password(password):
            login_user(u)
            return redirect(url_for('main.index'))
    return render_template("auth/login.html")

@auth.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username",None)
        email = request.form.get("email",None)
        password = request.form.get("pass",None)
        cpass = request.form.get("cpass",None)
        if username is not None and email is not None and password == password and password != None:
            u = User.query.filter_by(email=email).first()
            if u is not None:
                flash("Use with that email is already registered")
                return redirect(url_for('auth.register'))
            u = User(email=email,name=username,password=password)
            db.session.add(u)
            flash("User created successfully")
            return redirect(url_for('auth.login'))
        flash("all fields are required")
        return redirect(url_for('auth.register'))
    return render_template("auth/register.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))