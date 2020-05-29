import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from BLog import myEnvVal
from flask_admin import Admin
#myEnvVal.setVar()
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy import exc
from celery import Celery
from flask_jwt_extended import (JWTManager,create_access_token)
import time

myEnvVal.setVar()

while 1:
    try:
        e = create_engine('postgresql://%s:%s@%s:5432/%s' % (
    # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
    os.environ['DBUSER'], os.environ['DBPASS'], os.environ['DBHOST'], os.environ['DBNAME']
))
        e.execute('select 1')
    except exc.OperationalError:
        print('Waiting for database...')
        time.sleep(1)
    else:
        break

print('Connected!')



app = Flask(__name__)

app.config['SECRET_KEY'] = 'be9f24f348942bc26cd365c2fc86b769'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@%s:5432/%s' % (
    # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
    os.environ['DBUSER'], os.environ['DBPASS'], os.environ['DBHOST'], os.environ['DBNAME']
)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'


db = SQLAlchemy(app)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
cors = CORS(app)
celery=Celery(app.import_name,broker='redis://redis:6379/0')
admin = Admin(app, name='Express Daily', template_mode='bootstrap3')
bcrypt=Bcrypt(app)
jwt=JWTManager(app)
loginmanager = LoginManager(app)
loginmanager.login_view='users.login'
loginmanager.login_message_category='info'
app.config['MAIL_SERVER']= 'smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('Password')
mail=Mail(app)


from BLog.users.route import users
from BLog.posts.route import posts
from BLog.main.route import main
from BLog.errors.handler import errors


app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)
