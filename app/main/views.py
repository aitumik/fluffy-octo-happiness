from flask import render_template,redirect,url_for,request,flash
from flask_login import login_required
from . import main
from app import db
from app.models import User,Post

@main.route("/")
def index():
	posts = Post.query.order_by(Post.created_at.desc()).all()[:8]
	return render_template("index.html",posts=posts)

@main.route("/posts",methods=['GET','POST'])
@login_required
def posts():
	if request.method == 'POST':
		title = request.form.get("title",None)
		subtitle = request.form.get("subtitle",None)
		body = request.form.get("body",None)
		url = request.form.get("url",None)
		if url is None or title is None or body is None:
			flash("All fields are required")
			return redirect(url_for("main.posts"))
		post = Post.query.filter_by(title=title).first()
		if post is not None:
			flash("Post with that title already exists")
			return redirect(url_for('main.posts'))
		post = Post(title=title,subtile=subtitle,body=body,image_url=url)
		db.session.add(post)
	return render_template("posts.html")

@main.route("/post/<post_id>")
@login_required
def post(post_id):
	post = Post.query.get(int(post_id))
	return render_template("post.html",post=post)


@main.route("/")
def admin():
	return render_template("admin.html")
