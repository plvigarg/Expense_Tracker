from connect import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from connect import login_manager


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    name = db.Column(db.String(64))
    pasword_hash = db.Column(db.String(128))
    income = db.Column(db.Integer)
    budget = db.Column(db.Integer, default=0)
    profile_image = db.Column(
        db.String(128), nullable=False, default="default_profile.jpeg"
    )
    trans = db.relationship("Transactions", backref="User", lazy="dynamic")

    def check_password(self, password):
        return check_password_hash(self.pasword_hash, password)

    def _repr_(self):
        return f"Username {self.username}"


class Transactions(db.Model):

    __searchable__ = ["description", "cat", "amount", "date"]
    users = db.relationship(Users)
    id = db.Column(db.Integer, primary_key=True)
    cashFlow = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    description = db.Column(db.String(64))
    cat = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def _repr_(self):
        return f"amount : {self.amount}\
             ,cash : {self.cashFlow},\
                  description : {self.description},\
                       cat : {self.cat},\
                            date : {self.date} "
