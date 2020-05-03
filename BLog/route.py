from BLog.models import User, Post
from flask import  render_template, url_for, flash, redirect
from BLog.forms import RegistrationForm, LoginForm
from BLog import app,bcrypt,db
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
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_pw)
        
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can login now', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        list=User.query.all()
        cur_pass=""
        for user in list:
            if user.email==form.email.data:
                cur_pass=user.password
                break
        if  bcrypt.check_password_hash(cur_pass,form.password.data):
            flash('Welcome Niraj', 'success')
            return redirect(url_for('home'))
        else:
            flash("login unsuccessful, please check username and password!", 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/about")
def about():
    return "about"