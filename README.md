# Email Campaign Manager

Email Campaign Manager Django app for MikeLegal task.

# Pre-requisites
Install the pre-requisites using requirements.txt `pip install -r requirements.txt`

# How to run
* Clone the repo
* Install the pre-requisites
* Run the Django server
```
cd ECM
python manage.py runserver
```
* Open the browser and go to http://127.0.0.1:8000/

# Instructions

Virtual environment is already included in the repo

Admin credentials:
```
username: admin
password: admin
```

Manager is the app that is used for everything.

SMTP is configured in the settings.py file. Please use your own SMTP credentials. Currently the daily emails are sent out at 12:00 PM. You can change this accordingly.

And for prototyping purposes, I have included a custom command to manually trigger the daily mailing process. You can run it using the following command:
```
python manage.py send_email
```

# Endpoints
* `/`      : You are here
* `/unsub` : Unsubscribe page for the users
* `/test`  : Endpoint to send a test email to a user (for testing purposes)

