import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import (JWTManager,create_access_token)
# from BLog import myEnvVal
# myEnvVal.setVar()



app = Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = 'be9f24f348942bc26cd365c2fc86b769'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
ma=Marshmallow(app)
bcrypt=Bcrypt(app)
jwt=JWTManager(app)
loginmanager = LoginManager(app)
loginmanager.login_view='login'
loginmanager.login_message_category='info'
app.config['MAIL_SERVER']= 'smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail=Mail(app)
from BLog import route

