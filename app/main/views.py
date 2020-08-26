from flask import render_template,redirect,url_for,request,flash
from flask_login import login_required
from . import main
from app.models import User,Post

@main.route("/")
def index():
	posts = Post.query.all()
	return render_template("index.html",posts=posts)

@main.route("/posts")
@login_required
def posts():
	return render_template("posts.html")

@main.route("/")
def admin():
	return render_template("admin.html")
