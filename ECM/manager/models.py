from django.db import models
from django.utils import timezone

class Subscriber(models.Model):
    '''
    This model stores the details of a subscriber.
    '''
    email = models.EmailField(unique=True, verbose_name='Email') # This is the unique identifier
    first_name = models.CharField(max_length=255, verbose_name='First Name')

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

class Campaign(models.Model):
    '''
    This model stores the details of a campaign.
    '''
    campaign_id = models.AutoField(primary_key=True, verbose_name='Campaign ID') # This is the primary key
    name = models.CharField(max_length=255, unique=True, verbose_name='Campaign Name') # This is the unique identifier

    # The following are the fields that are required for a campaign email
    subject = models.CharField(max_length=255, verbose_name='Subject')
    preview_text = models.TextField(verbose_name='Preview Text')
    article_url = models.URLField(verbose_name='Article URL')
    html_content = models.TextField(verbose_name='HTML Content')
    plain_text_content = models.TextField(verbose_name='Plain Text Content')
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Published Date')

    class Meta:
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'

class Subscriptions(models.Model):
    '''
    This model stores the subscription status of a subscriber for a campaign.
    '''
    subscriber_email = models.ForeignKey(Subscriber, on_delete=models.CASCADE, verbose_name='Subscriber Email') # subscriber_email
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE, to_field='name', related_name='campaign_name', verbose_name='Campaign Name') # campaign_name
    is_subscribed = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        constraints = [
            models.UniqueConstraint(fields=['subscriber_email', 'campaign_name'], name='unique_subscription')
        ]