import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import loginForm, registrationForm, transactionForm, profiles
from models import Users
from flask_login import login_user, logout_user, login_required, current_user


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

    if RegistrationForm.validate_on_submit():
        user = Users(email=RegistrationForm.email.data,
                     username=RegistrationForm.username.data, password=RegistrationForm.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Thanks for registeration!')
        return redirect(url_for('index'))

    if loginForm.validate_on_submit():
        user = Users.query.filter_by(email=LoginForm.email.data).first()

        if user.check_password(LoginForm.password.data) and user is not None:

            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('dashboard')

            return redirect(next)
    return render_template('index.html', logForm=LoginForm, signForm=RegistrationForm)


