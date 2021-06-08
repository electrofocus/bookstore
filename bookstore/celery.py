import os

from django.core.mail import send_mail
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

app = Celery('bookstore')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def send_email_notification(self, email, message):
    print(f'Sending message {message} to email {email}')

    send_mail(
        subject='Book ordering',
        message=message,
        from_email='info@bookstore.com',
        recipient_list=[email],
        fail_silently=False,
    )
