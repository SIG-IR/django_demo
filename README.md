# Instructions to get started
- Don't clone this repo! The below commands will teach you how to make it yourself from scratch (at least how to get started)
```
django-admin startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile  electionsite
cd electionsite
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```