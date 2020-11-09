import os
from flask import Flask, render_template, session, redirect, url_for
from forms import loginForm, registrationForm, transactionForm, profiles
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)


app.config['SECRET_KEY'] = 'iceCream'

# DATABASE
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
def index():
    LoginForm = loginForm()
    RegistrationForm = registrationForm()
    # if loginForm.validate_on_submit():
    #
    #
    #
    return render_template('index.html', logForm=LoginForm, signForm=RegistrationForm)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    transForm = transactionForm()
    return render_template('dashboard.html', transForm=transForm)


@app.route('/passbook', methods=['GET', 'POST'])
def passbook():
    return render_template('passbook.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    proForm = profiles()
    return render_template('profile.html', proForm=proForm)


if __name__ == '__main__':
    app.run(debug=True)
