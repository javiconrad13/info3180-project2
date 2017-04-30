from flask_mail import Message
from app import app
from app.config import BaseConfig
from flask import Flask
from flask_mail import Mail

mail = Mail(app)
app.config.update(
	DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'leonfacey12345@gmail.com',
    MAIL_PASSWORD = 'lzlmosighfikucgh'
	)
mail = Mail(app)


def send_email(to, subject, id):
    msg = Message(
        subject,
        recipients=[to],
        html="Please click on the following link below to view the items on my wishlist: " + "  http://info-p2-leon101.c9users.io/api/user/"+ str(id) +"/wishlist",
        sender='leon.facey@gmail'
        # sender=app.config['MAIL_DEFAULT_SENDER']
        
    )
    mail.send(msg)