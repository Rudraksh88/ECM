"""
URL configuration for email_campaign_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manager.views import unsubscribe, send_email
import markdown
from django.shortcuts import render

def render_readme(request):
    return render(request, 'readme.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_readme, name='home'), # URL to render the readme.html file
    path('unsub', unsubscribe, name='unsubscribe'), # URL to unsubscribe
    path('test', send_email, name='send_email'), # Temporary URL to send a test email
]