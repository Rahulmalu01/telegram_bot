from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    send_mail(
        subject="Welcome!",
        message="Thanks for registering!",
        from_email="admin@example.com",
        recipient_list=[email],
    )
