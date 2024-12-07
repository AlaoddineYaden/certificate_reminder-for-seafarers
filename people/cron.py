from django_cron import CronJobBase, Schedule
from .utils import send_certificate_expiry_notifications  # Or wherever you put the notification function

class SendCertificateExpiryNotificationsJob(CronJobBase):
    schedule = Schedule(run_every_mins=1440)  # Run every day (1440 minutes)
    code = 'people.send_certificate_expiry_notifications'  # Unique code for the job

    def do(self):
        send_certificate_expiry_notifications()
