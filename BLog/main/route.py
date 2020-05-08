from flask import render_template,request,Blueprint
from BLog.models import Post

main=Blueprint("main",__name__)

@main.route("/")
@main.route("/index")
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=1)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    return "about"
 