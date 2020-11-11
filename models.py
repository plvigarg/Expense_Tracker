from connect import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from connect import login_manager


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):

    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    name = db.Column(db.String(64))
    pasword_hash = db.Column(db.String(128))
    trans = db.relationship('Transactions', backref='User', lazy='dynamic')

    def check_password(self, password):
        return check_password_hash(self.pasword_hash, password)

    def _repr_(self):
        return f"Username {self.username}"


class Transactions(db.Model):

    users = db.relationship(Users)
    id = db.Column(db.Integer, primary_key=True)
    cashFlow = db.Column(db.Boolean)
    amount = db.Column(db.Integer)
    description = db.Column(db.String(64))
    cat = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, cashFlow, amount, description, cat, date):
        self.cashFlow = cashFlow
        self.amount = amount
        self.description = description
        self.cat = cat
        self.date = date

    def _repr_(self):
        return f"amount : {self.amount}\
             ,cash : {self.cashFlow},\
                  description : {self.description},\
                       cat : {self.cat},\
                            date : {self.date} "
