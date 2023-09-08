from django.shortcuts import render
from manager.models import Subscriber, Campaign, Subscriptions
from django.template.loader import get_template
import smtplib
from email.mime.text import MIMEText

# Function to send daily emails
def send_daily_emails():
    plaintext = get_template('email.txt')
    htmly     = get_template('base.html')

    msg = MIMEText('Testing some Mailgun awesomness') # HTML email as string
    msg['Subject'] = "Hello"
    msg['From']    = "foo@YOUR_DOMAIN_NAME"
    msg['To']      = "bar@example.com"

    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login('postmaster@YOUR_DOMAIN_NAME', '3kh9umujora5')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()


# Function to render the unsubscribe page
def unsubscribe(request):
    if request.method == 'GET':
        return render(request, 'unsub_landing.html')

    if request.method == 'POST':
        # Get the email from the form
        email = request.POST.get('email')

        # Get the subscriber object
        subscriptions = Subscriptions.objects.filter(subscriber_email=email)

        no_subs = False

        # Check if the subscriber has any subscriptions in the first place
        if len(subscriptions) == 0:
            # User has no subscriptions
            no_subs = True
        else:
            # Unsubscribe the subscriber from all subscriptions
            for subscription in subscriptions:
                subscription.is_subscribed = False
                subscription.save()

        return render(request, 'unsubed.html', context={'no_subs': no_subs})