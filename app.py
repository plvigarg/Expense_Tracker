from flask import Flask, render_template, session, redirect, url_for
from forms import loginForm, registrationForm, transactionForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'iceCream'


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


@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)
