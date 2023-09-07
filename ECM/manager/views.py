from django.shortcuts import render

# Function to send daily emails
def send_daily_emails():
    pass

# Function to render the unsubscribe page
def unsubscribe(request):
    return render(request, 'unsub.html', context={})