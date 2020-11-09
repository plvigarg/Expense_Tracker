from connect import app
from flask import Flask, render_template, session, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from forms import loginForm, registrationForm, transactionForm, profiles
from models import Users


@app.route('/', methods=['GET', 'POST'])
def index():
    LoginForm = loginForm()
    RegistrationForm = registrationForm()

    if RegistrationForm.validate_on_submit():
        user = Users(email=RegistrationForm.email.data,
                     name=RegistrationForm.username.data, password=RegistrationForm.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Thanks for registeration!')
        return redirect(url_for('index'))

    elif LoginForm.validate_on_submit():
        user = Users.query.filter_by(email=LoginForm.email.data).first()

        if user.check_password(LoginForm.password.data) and user is not None:

            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('dashboard')

            return redirect(next)
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
