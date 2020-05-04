from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)
app.config['SECRET_KEY'] = 'be9f24f348942bc26cd365c2fc86b769'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
loginmanager = LoginManager(app)
loginmanager.login_view='login'
loginmanager.login_message_category='info'
from BLog import route

