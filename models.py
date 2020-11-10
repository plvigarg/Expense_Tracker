from connect import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from connect import login_manager


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    name = db.Column(db.String(64))
    pasword_hash = db.Column(db.String(128))
    # pasword = db.Column(db.String(128))
    # posts = db.relationship('BlogPost', backref='author', lazy=True)

    # def _init_(self, email, name, password):
    #     self.email = email
    #     self.name = name
    #     self.pasword_hash = password

    def check_password(self, password):
        return check_password_hash(self.pasword_hash, password)

    def _repr_(self):
        return f"Username {self.username}"
