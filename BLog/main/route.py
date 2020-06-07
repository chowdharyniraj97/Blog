from flask import render_template,request,Blueprint
from BLog.models import Post
from flask import jsonify

main=Blueprint("main",__name__)

@main.route("/")
@main.route("/index")
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=1)
    post=Post.query.all()
    all_post=[]
    for cur in post:
        post_dict=cur.__dict__
        del post_dict['_sa_instance_state']
        all_post.append(post_dict)
    return jsonify(all_post),200
   


@main.route("/about")
def about():
    return "about"
 