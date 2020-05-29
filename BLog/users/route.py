from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from BLog import db, bcrypt,jwt,celery
from flask import jsonify,json
from flask_jwt_extended import (create_access_token)
from BLog.models import User, Post
from BLog.users.forms import (RegistrationForm, LoginForm, UpdateForm,
                                   RequestResetForm, ResetPasswordForm)
from BLog.users.utils import save_pic, send_email

users=Blueprint('users',__name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        data=request.get_json()
        hashed_pw=bcrypt.generate_password_hash(data['password']).decode('utf-8')
        user=User(username=data['username'],email=data['email'],password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        # print('user added')
        # print(request)
        result={'email':user.email+" registered"}
        return jsonify({"result":result}),201

@users.route("/login", methods=['GET', 'POST'])
def login():
    print(current_user)
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    print("hello")
    if request.method =='POST':
        data=request.get_json()
        # print(data)
        user=User.query.filter_by(email=data['email']).first()
        print(user)
        password=data['password']
        print(user.password)
        print(data)
        print(bcrypt.check_password_hash(user.password,password))
        if user and bcrypt.check_password_hash(user.password,password):
            access_token=create_access_token(identity={
                'username':user.username,
                'email':user.email
            })
            # print(access_token)
            result=jsonify({'token':access_token})
        
        else:
            result =jsonify({'error':'invalid username password'}),405

    else:
        return render_template('login.html', title='Login',form=form)
    return result

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
    data=request.get_json()
    print(data)
    reset.delay(data['email'])
    return jsonify({'message':'email sent'})


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


@celery.task
def reset(email):
    user = User.query.filter_by(email=email).first()
    send_email(user,email)