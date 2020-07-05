# Lecture Notes for Djanjo lecture
This is a note written by @noklam for personal use for the CS50W lectures.

# Notes
* Django is a "project" which runs multiple apps within it. Each app serves it own purpose and can interact with each other.
* Add Apps to INSTALLED_APP in `settings.py`
* <str:name> custom dynamic route

# Get Started
```
django-admin startproject lecture3_nc
cd lecture3_nc
python manage.py runserver

## Create your first app
```
python manage.py startapp hello
```