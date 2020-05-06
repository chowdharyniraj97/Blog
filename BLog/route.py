import os,secrets
from BLog.models import User, Post
from flask import  render_template, url_for, flash, redirect, request
from BLog.forms import RegistrationForm, LoginForm, UpdateForm
from BLog import app,bcrypt,db
from flask_login import login_user,current_user,logout_user,login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
       user=User.query.filter_by(email=form.email.data).first()
       
       if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            if next_page:
                return redirect(url_for(next_page))
            else:
                flash(f'Welcome {user.username}', 'success')
                return redirect(url_for("home"))
       else:
            flash("Login unsuccessful, please check username and password!", 'danger')

    return render_template('login.html', title='Login', form=form)

def save_pic(form_pic):
    random_hex=secrets.token_hex(8)
    _,f_ext=os.path.splitext(form_pic.filename)
    picture_fn=random_hex+f_ext
    pict_path=os.path.join(app.root_path,'static/profile_pic',picture_fn)
    form_pic.save(pict_path)
    return picture_fn

@app.route("/about")
def about():
    return "about"

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form=UpdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file=save_pic(form.picture.data)
            current_user.image_file=picture_file


        current_user.username=form.username.data
        current_user.email=form.email.data  
        db.session.commit()
        flash('Your accout has been updated successfully','success')   
        return redirect(url_for('account'))
    image_file=url_for('static',filename='profile_pic/'+current_user.image_file)
    return render_template('account.html', title='Account',image_file=image_file,form=form)
