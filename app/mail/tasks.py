from celery import shared_task

from user import models as user_models
from mail.mail import MailsApp


@shared_task(name="send_verify_email")
def send_verify_email_task(user_id, code):
    user = user_models.User.objects.filter(id=user_id).first()
    if user is None:
        return

    mail = MailsApp().verify_email(user, code)
    mail.send()

    if mail.error_message:
        print(mail.error_message)


@shared_task(name="send_password_reset_request_email")
def send_password_reset_request_email_task(user_id, code):
    print("send_password_reset_request_email_task")
    user = user_models.User.objects.filter(id=user_id).first()
    if user is None:
        return

    mail = MailsApp().password_reset_request(user, code)
    mail.send()

    if mail.error_message:
        print(mail.error_message)

