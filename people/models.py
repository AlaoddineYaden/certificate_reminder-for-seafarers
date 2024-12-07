from django.db import models
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from django.db.models import UniqueConstraint

# Models
class CertificateType(models.Model):
    """Predefined list of certificate types."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    """Represents a person with basic information."""
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class PersonCertificate(models.Model):
    """Represents a certificate held by a person with an expiration date."""
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="certificates")
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)
    expiration_date = models.DateField()

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['person', 'certificate_type'], name='unique_person_certificate'
            )
        ]

    def __str__(self):
        return f"{self.person.name} - {self.certificate_type.name} (Expires: {self.expiration_date})"