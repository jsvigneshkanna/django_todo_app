# django_todo_app

Hey 👋🏻, am building new Django app through learning from many resources. Come lets all learn together🚀

---

## Django setup

1. Make a new folder
   > `mkdir django-app`
2. Navigate to new folder
   > `cd django-app`
3. Install pipenv(virtual environment) using pip
   > `pip install pipenv`
4. Activate a new virtual environment
   > `pipenv shell`
5. Install Django in new virtual env
   > `pip install django`
6. Create new django project
   > `django-admin startproject projectname`
7. Navigate to newly created django project
   > `cd projectname`
8. Start a new django app
   > `python manage.py startapp appname`
9. Run migrations
   > `python manage.py migrate`
10. Start the server and test
    > `python manage.py runserver`
11. Add the django app to django project settings.py
    > `projectname/settings.py`
12. Navigate to newly djangoapp and create models.py to create database structure
13. Once models are changes run below cmd for migrations
    > `python manage.py makemigrations appname`
14. Apply the changes to the database
    > `python manage.py migrate appname

## Django references docs

1. [Django official docs](https://www.djangoproject.com/start/)
2. [Digital ocean django react app integrations](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)
