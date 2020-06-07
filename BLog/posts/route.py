from flask import Blueprint, request
from flask import jsonify
from BLog import db
from BLog.models import Post, User

posts = Blueprint("posts", __name__)


# single post route
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


# adding new post
@posts.route("/post/new", methods=['GET', 'POST'])
def new_posts():
    data = request.get_json()
    print(data)
    user = User.query.filter_by(email=data['email']).first()
    post = Post(title=data['title'], content=data['content'], author=user)
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post added'})


# updating post route
@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify({'message': 'successs'})


# deleting post route
@posts.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'post deleted'})
