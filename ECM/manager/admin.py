from django.contrib import admin

# Register your models here.
from .models import Subscriber, Campaign, Subscriptions, CampaignEmail

admin.site.register(Subscriber, list_display=['email', 'first_name'])
admin.site.register(Campaign, list_display=['campaign_id', 'name', 'created_by'])
admin.site.register(Subscriptions, list_display=['subscriber_email', 'campaign_name', 'is_subscribed'])
admin.site.register(CampaignEmail, list_display=['campaign', 'subject', 'preview_text', 'published_date'])