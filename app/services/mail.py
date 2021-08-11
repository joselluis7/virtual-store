from app.extension import mail
from flask import current_app, render_template
from flask_mail import Message


def send_mail(subject, to, template, **kwargs):

    msg = Message(
        subject=subject, recipients=[to], sender=current_app.config["MAIL_SENDER"]
    )
    msg.body = render_template(f"mail/{template}.txt", **kwargs)
    msg.html = render_template(f"mail/{template}.html", **kwargs)
    mail.send(msg)
