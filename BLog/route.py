import os,secrets
from PIL import Image
from BLog.models import User, Post
from flask import  render_template, url_for, flash, redirect, request,abort
from BLog.forms import RegistrationForm, LoginForm, UpdateForm,PostForm
from BLog import app,bcrypt,db
from flask_login import login_user,current_user,logout_user,login_required

@app.route("/")
@app.route("/index")
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.paginate(page=page,per_page=1)
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
    output_size=(125,125)
    i=Image.open(form_pic)
    i.thumbnail(output_size)
    i.save(pict_path)
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


@app.route("/post/new",methods=['GET', 'POST'])
@login_required
def new_posts():
    form=PostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created','success')
        return redirect(url_for("home"))
    return render_template('creat_post.html', title='New Post',form=form,legend="New Post")

@app.route("/post/<int:post_id>")
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html',title=post.title,post=post)

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
