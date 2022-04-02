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




# Changelog
* v0.0.1 django initialized

