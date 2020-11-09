from flask import Flask, render_template, session, redirect, url_for













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
