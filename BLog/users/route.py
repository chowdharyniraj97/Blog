from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from BLog import db, bcrypt
from BLog.models import User, Post
from BLog.users.forms import (RegistrationForm, LoginForm, UpdateForm,
                                   RequestResetForm, ResetPasswordForm)
from BLog.users.utils import save_pic, send_email

users=Blueprint('users',__name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_pw)
        
        db.session.add(user)
        db.session.commit()
        flash('Account created for You can login now', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
       user=User.query.filter_by(email=form.email.data).first()
       
       if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            if next_page:
                return redirect(url_for(next_page))
            else:
                #flash(f'Welcome {user.username}', 'success')
                return redirect(url_for("main.home"))
       else:
            flash("Login unsuccessful, please check username and password!", 'danger')

    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/account", methods=['GET', 'POST'])
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
        return redirect(url_for('users.account'))
    image_file=url_for('static',filename='profile_pic/'+current_user.image_file)
    return render_template('account.html', title='Account',image_file=image_file,form=form)

@users.route("/user/<string:username>")
def user_posts(username):
    page=request.args.get('page',1,type=int)
    user=User.query.filter_by(username=username).first_or_404()
    posts=Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page,per_page=1)
    return render_template("user_posts.html", posts=posts,user=user)

@users.route("/reset_password",methods=['POST','GET'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form=RequestResetForm()

    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        send_email(user)
        flash("an Email has been sent to your mailbox",'info')
        return redirect(url_for('users.login'))
    return render_template("reset_request.html",title="Reset Password",form=form)

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
