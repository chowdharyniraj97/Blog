import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from BLog import mail,app

def send_email(user,email):
    
    with app.test_request_context():

        msg=Message('Password Reset Request',sender='noreply@expressdaily.com',recipients=[email])
        msg.body=f'''To Reset your password visit the following link:
    xyz.com
    If you did not make ignore!!
    '''
        mail.send(msg)
