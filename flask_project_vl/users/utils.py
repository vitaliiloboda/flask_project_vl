import os
from secrets import token_hex
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flask_project_vl import mail


def save_picture(form_picture):
    random_hex = token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Reset password request',
                  sender='badrhymes@yandex.ru',
                  recipients=[user.email])
    msg.body = f'''To reset password please go through next link: 
                {url_for('users.reset_token', token=token, _external=True)}. 
                If you hasn't done this request please ignore this letter.'''
    mail.send(msg)

