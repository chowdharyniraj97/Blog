import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from BLog import mail,app

def send_email(user):
    print(user)
    print(user.email)
    with app.test_request_context():

        msg=Message('Password Reset Request',sender='noreply@expressdaily.com',recipients=[user.email])
        msg.body=f'''To Reset your password visit the following link:
    xyz.com
    If you did not make ignore!!
    '''
        mail.send(msg)

def save_pic(form_pic):
    random_hex=secrets.token_hex(8)
    _,f_ext=os.path.splitext(form_pic.filename)
    picture_fn=random_hex+f_ext
    pict_path=os.path.join(app.root_path,'static/profile_pic',picture_fn)
    output_size=(125,125)
    i=Image.open(form_pic)
    i.thumbnail(output_size)
    i.save(pict_path)
    return picture_fn
