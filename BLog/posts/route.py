from flask import Blueprint, request, url_for, flash, render_template, abort, redirect
from flask_login import current_user, login_required
from flask import jsonify, json
from flask_jwt_extended import (create_access_token)
from BLog import db
from BLog.models import Post, User
from BLog.posts.forms import PostForm

posts = Blueprint("posts", __name__)


@posts.route('/post/<int:postid>', methods=['GET', 'POST'])
def one_posts(postid):
    post = Post.query.filter_by(id=postid).first();
    res = {
        'id': post.id,
        'title': post.title,
        'date': post.date_posted,
        'content': post.content,
        'user_id': post.user_id

    }
    return jsonify({'post': res})


@posts.route("/post/new", methods=['GET', 'POST'])
def new_posts():
    data = request.get_json()
    print(data)
    user = User.query.filter_by(email=data['email']).first()
    post = Post(title=data['title'], content=data['content'], author=user)
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post added'})


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify({'message': 'successs'})


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return jsonify({'message':'post deleted'})
