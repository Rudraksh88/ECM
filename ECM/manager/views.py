from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import threading

def send_email_to_subscribers(recipient, email):
    '''
    Function to send emails to subscribers in parallel
    '''
    from email_campaign_manager.settings import EMAIL_HOST_USER
    html_message = render_to_string('email_template.html', {'campaign_email': email})

    send_mail(
        subject=email.subject,
        message=strip_tags(html_message),
        from_email=EMAIL_HOST_USER,
        recipient_list=[recipient],
        fail_silently=False,
        html_message=html_message
    )

def send_emails_in_parallel(subscribers, campaign_emails):
    '''
    Function to send emails using threading
    '''
    threads = [] # List to store threads

    # Iterate over subscribers and send emails in parallel
    for subscriber in subscribers:

        # Iterate over campaign emails and send emails in parallel
        for email in campaign_emails:
            print(email) # Debug print when manually triggering the daily sending of emails
            thread = threading.Thread(target=send_email_to_subscribers, args=(subscriber.subscriber_email.email, email))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

def send_daily_emails():
    '''
    Function to send daily emails
    '''
    # Get the current date in the project's timezone
    today = timezone.localdate()

    from manager.models import Subscriber, Campaign, Subscriptions, CampaignEmail

    # Retrieve all campaign names that have new emails to send
    campaigns_with_new_emails = Campaign.objects.filter(
        campaign_name_email__published_date__date=today
    ).distinct()

    # Iterate over campaigns with new emails
    for campaign in campaigns_with_new_emails:

        # Retrieve all subscribers for this campaign that are subscribed
        subscribers = Subscriptions.objects.filter(
            campaign_name=campaign,
            is_subscribed=True  # Only send emails to subscribed users
        )

        # Retrieve all campaign emails for this campaign that were published today
        campaign_emails = CampaignEmail.objects.filter(campaign=campaign, published_date__date=today)

        send_emails_in_parallel(subscribers, campaign_emails)

    return True

def unsubscribe(request):
    '''
    Function to render the unsubscribe page
    '''
    if request.method == 'GET':
        return render(request, 'unsub_landing.html')

    if request.method == 'POST':
        # Get the email from the form
        email = request.POST.get('email')

        # Get the subscriber object
        from manager.models import Subscriptions
        subscriptions = Subscriptions.objects.filter(subscriber_email=email)

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

# Function to send a test email
def send_email(request):
    from email_campaign_manager.settings import EMAIL_HOST_USER
    send_mail(
        subject = 'Thats your subject',
        message = 'Thats your message body',
        from_email=EMAIL_HOST_USER,
        recipient_list = [''],
        fail_silently = False,
        html_message = '<h1>This is a test</h1>'
    )

    return HttpResponse('Email sent')