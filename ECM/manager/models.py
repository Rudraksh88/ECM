from django.db import models
from django.utils import timezone

class Subscriber(models.Model):
    '''
    This model stores the details of a subscriber.
    '''
    email = models.EmailField(unique=True) # This is the unique identifier
    first_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

class Campaign(models.Model):
    '''
    This model stores the details of a campaign.
    '''
    campaign_id = models.AutoField(primary_key=True) # This is the primary key
    campaign_name = models.CharField(max_length=255, unique=True) # This is the unique identifier

    # The following are the fields that are required for a campaign email
    subject = models.CharField(max_length=255)
    preview_text = models.TextField()
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'

class Subscriptions(models.Model):
    '''
    This model stores the subscription status of a subscriber for a campaign.
    '''
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE) # subscriber_email
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE) # campaign_id
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE, to_field='campaign_name', related_name='campaign_name') # campaign_name
    is_subscribed = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        unique_constraints = [
            models.UniqueConstraint(fields=['subscriber', 'campaign_id'], name='unique_subscription')
        ]