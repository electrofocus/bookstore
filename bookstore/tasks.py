from django.core.mail import send_mail

from bookstore import celery_app


@celery_app.task(bind=True)
def send_email_task(self, email, message):
    send_mail(
        subject='Book ordering',
        message=message,
        from_email='qlgf3onpum@gmail.com',
        recipient_list=[email],
        fail_silently=False,
    )
