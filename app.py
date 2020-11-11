from connect import app,db
from flask import Flask, render_template, session, redirect, url_for,request
from flask_login import login_user, logout_user, login_required, current_user
from forms import loginForm, registrationForm, transactionForm, profiles
from models import Users,Transactions
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/', methods=['GET', 'POST'])
def index():

    RegistrationForm = registrationForm()
    LoginForm = loginForm()

    if RegistrationForm.validate_on_submit():
        passw = generate_password_hash(RegistrationForm.password2.data)

        user = Users(email=RegistrationForm.email2.data,
                     name=RegistrationForm.username2.data, pasword_hash=passw)

        db.session.add(user)
        db.session.commit()
        print('Thanks for registeration!')
        return redirect(url_for('index'))

    if LoginForm.validate_on_submit():
        user = Users.query.filter_by(email=LoginForm.email1.data).first()

        if user is not None and user.check_password(LoginForm.password1.data):

            login_user(user)
            # flash('Log in Success!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('dashboard')

            return redirect(next)
    return render_template('index.html', logForm=LoginForm, signForm=RegistrationForm)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    transForm = transactionForm()

    if transForm.validate_on_submit():
        print("In form")
        data = Transactions(cashFlow=transForm.flow.data,
                     amount=transForm.amount.data, description=transForm.description.data,cat=transForm.category.data,\
                         date=transForm.date.data, userId=current_user.id)

        db.session.add(data)
        db.session.commit()
        # flash()
        print("data send")
        return redirect(url_for('dashboard'))

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
