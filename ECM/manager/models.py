from django.db import models
from django.utils import timezone
from django.conf import settings

class Subscriber(models.Model):
    '''
    This model stores the details of a subscriber.
    '''
    email = models.EmailField(unique=True, verbose_name='Email', primary_key=True) # This is the unique identifier
    first_name = models.CharField(max_length=255, verbose_name='First Name')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

class Campaign(models.Model):
    '''
    This model stores the details of a campaign.
    '''
    campaign_id = models.AutoField(primary_key=True, verbose_name='Campaign ID') # This is the primary key
    name = models.CharField(max_length=255, unique=True, verbose_name='Campaign Name') # This is the unique identifier
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', on_delete=models.CASCADE, verbose_name='Campaign Author') # created_by

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'


class Subscriptions(models.Model):
    '''
    This model stores the subscription status of a subscriber for a campaign.
    '''
    subscriber_email = models.ForeignKey(Subscriber, to_field='email', on_delete=models.CASCADE, verbose_name='Subscriber Email') # subscriber_email
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE, to_field='name', related_name='campaign_name', verbose_name='Campaign Name') # campaign_name
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.subscriber_email} | {self.campaign_name}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        constraints = [
            models.UniqueConstraint(fields=['subscriber_email', 'campaign_name'], name='unique_subscription')
        ]

class CampaignEmail(models.Model):
    # Each Campaign has 'Subject', 'preview_text', 'article_url', 'html_content', 'plain_text_content', 'published_date'.

    '''
    This model stores the details of a campaign email.
    '''

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, to_field='name', related_name='campaign_name_email', verbose_name='Campaign Name') # campaign_name
    subject = models.CharField(max_length=255, verbose_name='Subject')
    preview_text = models.CharField(max_length=255, verbose_name='Preview Text')
    article_url = models.URLField(max_length=255, verbose_name='Article URL')
    html_content = models.TextField(verbose_name='HTML Content')
    plain_text_content = models.TextField(verbose_name='Plain Text Content')
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Published Date')

    def __str__(self):
        return f'{self.campaign} | {self.subject}'

    class Meta:
        verbose_name = 'Campaign Email'
        verbose_name_plural = 'Campaign Emails'
        constraints = [
            models.UniqueConstraint(fields=['campaign', 'subject'], name='unique_campaign_email')
        ]
