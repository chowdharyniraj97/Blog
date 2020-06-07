from flask import render_template, request, Blueprint
from BLog.models import Post
from flask import jsonify

main = Blueprint("main", __name__)

# to get all posts route
@main.route("/")
@main.route("/index")
def home():
    post = Post.query.all()
    all_post = []
    for cur in post:
        post_dict = cur.__dict__
        del post_dict['_sa_instance_state']
        all_post.append(post_dict)
    return jsonify(all_post), 200

