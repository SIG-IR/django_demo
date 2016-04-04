# Instructions for you to get started
- Don't clone this repo! The below commands will teach you how to make it yourself from scratch (at least how to get started)
```
django-admin startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile  electionsite
cd electionsite
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

# Using this Application
- If you do want to use this application yourself, follow these instructions:
```
git clone https://github.com/sameetandpotatoes/Django-Tutorial
cd Django-Tutorial
pip install -r requirements.txt
```

Change `settings.py` and input your relevant Postgres database credentials, and `engine/seed.py` to change the candidates you're searching for

# API keys

To manage manage multiple sets of API keys both locally and on Heroku, I created a quick Python script in `serializer.py` to make it easy to create environment variables. Create a `secrets.py` in the root directory: ALCHEMY_CODES array and TWITTER_CODES hash with keys CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, and ACCESS_SECRET. Then run `python serializer.py` and follow the instructions there.

Then,
```
python manage.py migrate
python manage.py seed
python manage.py fetch
python manage.py runserver
```