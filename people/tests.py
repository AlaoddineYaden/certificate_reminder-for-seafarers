from django.test import TestCase
from django.core import mail
from datetime import date, timedelta
from people.models import CertificateType, Person, PersonCertificate
from people.views import send_certificate_expiry_notifications

class NotificationTestCase(TestCase):
    def setUp(self):
        self.certificate_type = CertificateType.objects.create(name="Safety Training")
        self.person = Person.objects.create(name="John Doe", email="alaoddineyaden223@gmail.com")
        self.certificate = PersonCertificate.objects.create(
            person=self.person,
            certificate_type=self.certificate_type,
            expiration_date=date.today() + timedelta(days=5)
        )

    def test_notification_email_sent(self):
        send_certificate_expiry_notifications()
        self.assertEqual(len(mail.outbox), 2)  # One to the person, one to the admin
        self.assertIn("Certificate Expiration Reminder", mail.outbox[0].subject)
