# Django Sessions Practice

# Step 1: Virtual Environment
`python3 -m venv venv`
`source venv/bin/activate`

## Step 2: Install Dependencies and Freeze to requirements.txt
`python3 -m pip install django djangorestframework`
`python3 -m pip freeze > requirements.txt`

Note: others can install the dependencies with this code: 
`python -m pip install -r requirements.txt`

## Step 3: Create Django Project
open project folder and init django with: 
`django-admin startproject server .`
`python3 manage.py migrate`
`python3 manage.py runserver`

--- v0.0.1 end ---

`python manage.py startapp api`
ADD rest_framework and api apps @ server/settings.py
ADD view @ api/views.py
ADD urls.py file @ core/urls.py
EDIT urls @ server/urls.py

--- v0.0.2 end ---

EDIT view @ api/views.py, sessions is used for visit count track

--- v0.0.3 end ---

ADD Task model @ api/models.py
ADD TaskSerializer @ api/serializers.py
ADD view route /api/task/
ADD Task model to admin page 

# Changelog
* v0.0.1 django initialized
* v0.0.2 drf test view
* v0.0.3 session cookie init
* v0.0.4 task model added