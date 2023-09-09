import django
from django.core.management.base import BaseCommand
from manager.views import send_daily_emails  # Import the email sending function

class Command(BaseCommand):
    '''
    Manually trigger the daily sending of emails

    Usage: python manage.py send_email
    '''

    help = 'Manually trigger the daily sending of emails'

    def handle(self, *args, **kwargs):
        django.setup()  # Initialize the Django application
        send_daily_emails()
        self.stdout.write(self.style.SUCCESS('Successfully triggered daily emails.'))
