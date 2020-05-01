from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Niraj Chowdhary',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Nikhil Chowdhary',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    }
]
@app.route("/")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return "about"
