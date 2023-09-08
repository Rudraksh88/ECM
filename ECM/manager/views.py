from django.shortcuts import render
from manager.models import Subscriber, Campaign, Subscriptions
from django.template.loader import get_template
import smtplib
from email.mime.text import MIMEText

# Function to send daily emails
def send_daily_emails():
    return True

# Function to render the unsubscribe page
def unsubscribe(request):
    if request.method == 'GET':
        return render(request, 'unsub_landing.html')

    if request.method == 'POST':
        # Get the email from the form
        email = request.POST.get('email')
        print('Email form resp:',email)

        # Get the subscriber object
        subscriptions = Subscriptions.objects.filter(subscriber_email=email)
        print('Subscriptions object:',subscriptions)

        no_subs = False

        # Check if the subscriber has any subscriptions in the first place
        if not subscriptions:
            # User has no subscriptions
            no_subs = True
        else:
            # Unsubscribe the subscriber from all subscriptions
            for subscription in subscriptions:
                subscription.is_subscribed = False
                subscription.save()

        return render(request, 'unsubbed.html', context={'no_subs': no_subs})