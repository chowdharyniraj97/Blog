import os,secrets
from flask import jsonify,json
from PIL import Image
from BLog.models import User, Post,PostSchema,UserSchema
from flask import  render_template, url_for, flash, redirect, request,abort
from BLog.forms import (RegistrationForm, LoginForm, UpdateForm,
                             PostForm, RequestResetForm, ResetPasswordForm)
from BLog import app,bcrypt,db,mail,jwt
from flask_login import login_user,current_user,logout_user,login_required
from flask_mail import Message
from flask_jwt_extended import (create_access_token)




@app.route("/")
@app.route("/index")
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=1)
    post=Post.query.all()
    all_post=[]
    for cur in post:
        post_dict=cur.__dict__
        del post_dict['_sa_instance_state']
        all_post.append(post_dict)
    return jsonify(all_post)
   
    


@app.route("/register", methods=['GET', 'POST'])
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

    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    # form = RegistrationForm()

    # # if form.validate_on_submit():
    # #     hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        
        
    # #     flash(f'Account created for {form.username.data}! You can login now', 'success')
    # #     return redirect(url_for('login'))
    # return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
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

@app.route("/post/new",methods=['GET', 'POST'])
def new_posts():
    data=request.get_json()
    print(data)
    user=User.query.filter_by(email=data['email']).first()    
    post=Post(title=data['title'],content=data['content'],author=user)
    db.session.add(post)
    db.session.commit()
    return jsonify({'message':'Post added'})

@app.route("/post/<int:post_id>")
def post(post_id):

    post=Post.query.get_or_404(post_id)
    post_dict=post.__dict__
    del post_dict['_sa_instance_state']
    print(post_dict)
    return jsonify({'message': post_dict})


    

@app.route("/post/<int:post_id>/update",methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    form=PostForm()
    if form.validate_on_submit():
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()
        flash("Your post has been updated")
        return redirect(url_for('post',post_id=post.id))

    elif request.method=='GET':
        form.title.data=post.title
        form.content.data=post.content

    form.title.data=post.title
    form.content.data=post.content
    return render_template('creat_post.html', title='Update Post',form=form,legend="Update Post")

@app.route("/post/<int:post_id>/delete",methods=['POST'])
def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted",'success')
    return redirect(url_for('home'))

@app.route("/user/<string:username>")
def user_posts(username):
    page=request.args.get('page',1,type=int)
    user=User.query.filter_by(username=username).first_or_404()
    posts=Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page,per_page=1)
    return render_template("user_posts.html", posts=posts,user=user)



