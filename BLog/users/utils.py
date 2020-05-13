import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from BLog import mail

def send_email(user):
    token=user.get_reset_token()
    print(user.email)
    msg=Message('Password Reset Request',sender='noreply@expressdaily.com',recipients=[user.email])
    msg.body=f'''To Reset your password visit the following link:
{url_for('reset_token',token=token,_external=True)}
If you did not make ignore!!
'''
    mail.send(msg)

def save_pic(form_pic):
    random_hex=secrets.token_hex(8)
    _,f_ext=os.path.splitext(form_pic.filename)
    picture_fn=random_hex+f_ext
    pict_path=os.path.join(current_app.root_path,'static/profile_pic',picture_fn)
    output_size=(125,125)
    i=Image.open(form_pic)
    i.thumbnail(output_size)
    i.save(pict_path)
    return picture_fn