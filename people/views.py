from celery import shared_task
import logging
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from people.models import PersonCertificate
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


logger = logging.getLogger(__name__)

@shared_task
def send_certificate_expiry_notifications():
    """Send notifications to persons and admins about expiring certificates."""
    today = timezone.now().date()
    one_week_from_now = today + timedelta(days=7)

    # Find certificates expiring within the next week
    expiring_certificates = PersonCertificate.objects.filter(
        expiration_date__range=[today, one_week_from_now]
    )

    admin_emails = User.objects.filter(is_staff=True).values_list('email', flat=True)

    for cert in expiring_certificates:
        person = cert.person
        certificate_name = cert.certificate_type.name
        expiration_date = cert.expiration_date

        # Notify the person about the expiring certificate
        if person.email:
            try:
                person_email_body = render_to_string('emails/person_certificate_expiry.html', {
                    'person': person,
                    'certificate_name': certificate_name,
                    'expiration_date': expiration_date
                })
                person_email = EmailMessage(
                    'Certificate Expiration Reminder',
                    person_email_body,
                    'your-email@example.com',
                    [person.email]
                )
                person_email.content_subtype = 'html'
                person_email.send()
                logger.info(f"Notification sent to {person.email} for certificate {certificate_name}")
            except Exception as e:
                logger.error(f"Failed to send email to {person.email}: {e}")

        # Notify all admins
        try:
            admin_email_body = render_to_string('emails/admin_certificate_expiry.html', {
                'person': person,
                'certificate_name': certificate_name,
                'expiration_date': expiration_date
            })
            admin_email = EmailMessage(
                'Certificate Expiring Soon (Admin Reminder)',
                admin_email_body,
                'your-email@example.com',
                admin_emails
            )
            admin_email.content_subtype = 'html'
            admin_email.send()
            logger.info(f"Admin notifications sent for {person.name} and certificate {certificate_name}")
        except Exception as e:
            logger.error(f"Failed to send admin notifications for {person.name}: {e}")
