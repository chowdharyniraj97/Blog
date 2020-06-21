import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from BLog import mail,app

def send_email(user,email):
    token=user.get_reset_token()
    with app.app_context():

        msg=Message('Password Reset Request',sender='noreply@expressdaily.com',recipients=[email])
        msg.body=f'''To Reset your password visit the following link:
    http://localhost/change_password/{token}
    If you did not make ignore!!
    '''
        mail.send(msg)
