from django.contrib import admin

# Register your models here.
from .models import Subscriber, Campaign, Subscriptions

admin.site.register(Subscriber, list_display=['email', 'first_name'])
admin.site.register(Campaign, list_display=['campaign_id', 'campaign_name', 'subject', 'preview_text', 'article_url', 'published_date'])
admin.site.register(Subscriptions, list_display=['subscriber', 'campaign', 'is_subscribed'])