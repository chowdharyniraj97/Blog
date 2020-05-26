from flask import Blueprint, request, url_for,flash,render_template,abort,redirect
from flask_login import current_user,login_required
from flask import jsonify,json
from flask_jwt_extended import (create_access_token)
from BLog import db
from BLog.models import Post,User
from BLog.posts.forms import PostForm

posts=Blueprint("posts",__name__)

@posts.route("/post/new",methods=['GET', 'POST'])
def new_posts():
    data=request.get_json()
    print(data)
    user=User.query.filter_by(email=data['email']).first()    
    post=Post(title=data['title'],content=data['content'],author=user)
    db.session.add(post)
    db.session.commit()
    return jsonify({'message':'Post added'})

@posts.route("/post/<int:post_id>/update",methods=['GET', 'POST'])
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
        return redirect(url_for('posts.post',post_id=post.id))

    elif request.method=='GET':
        form.title.data=post.title
        form.content.data=post.content

    form.title.data=post.title
    form.content.data=post.content
    return render_template('creat_post.html', title='Update Post',form=form,legend="Update Post")

@posts.route("/post/<int:post_id>/delete",methods=['POST'])
def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted",'success')
    return redirect(url_for('main.home'))