from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'be9f24f348942bc26cd365c2fc86b769'
posts = [
    {
        'author': 'Niraj Chowdhary',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Nikhil Chowdhary',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    }
]
@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'chowdharyniraj97@gmail.com' and form.password.data == 'password':
            flash('Welcome Niraj', 'success')
            return redirect(url_for('home'))
        else:
            flash("login unsuccessful, please check username and password!", 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/about")
def about():
    return "about"
