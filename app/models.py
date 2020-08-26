from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,AnonymousUserMixin
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100),unique=True)
    email = db.Column(db.String(128),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship("Post",backref="user",lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("password attribute is not readable")
    
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return "<User {}".format(self.name)

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    description = db.Column(db.String(100))
    price = db.Column(db.Integer,default=0)
    
    def __repr__(self):
        return "<Product {}".format(self.name)

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),unique=True)
    subtile = db.Column(db.Text)
    body = db.Column(db.Text)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def __repr__(self):
        return "<Post {}".format(self.body)