from celery import shared_task
from .views import send_certificate_expiry_notifications

@shared_task
def send_certificate_expiry_notifications_task():
    send_certificate_expiry_notifications()
