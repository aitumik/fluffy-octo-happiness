from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(128),unique=True,index=True)
    password_hash = db.Column(db.String(128))

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
