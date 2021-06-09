from django.core.mail import send_mail

from bookstore import celery_app
from store.models import Order


@celery_app.task(bind=True)
def send_email_task(self, email, message, order_id):
    send_mail(
        subject='Book ordering',
        message=message,
        recipient_list=[email],
        fail_silently=False,
        from_email=None,
    )
    Order.objects.filter(id=order_id).update(is_notified=True)
