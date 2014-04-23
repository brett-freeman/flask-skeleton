flask-skeleton
==============

A simple skeleton for quickly setting up a flask app. Utilizes blueprints for views and flask-sqlalchemy for the ORM

All package dependencies needed to get up and running are included in requirements.txt

Version 2.0 now uses blueprints in place of flask-classy, as well as highly improved structure.

Blueprint provided is named 'default' and is a simple placeholder for you to build from.

The following environment variables are suggested to be set. If the database URLs are not set, the application will default to a sqlite database stored in the root of the application directory named data-x.sqlite where x is the current config name.  
  
SECRET_KEY  
DEV_DATABASE_URL  
PRODUCTION_DATABASE_URL  
FLASK_CONFIG (will be development, testing, production or default)  

installation
============
It's suggested to always use a virtual environment with each application.

git clone https://github.com/port-/flask-skeleton.git  
pip install -r requirements.txt  
python manage.py runserver  

structure
=========

app/  
__\-__ templates/  
__--__ default/ _(templates for default blueprint)_  
__---__ index.html  
__--__ base.html _(base template, calls bootstrap, all other templates inherit from this)_  
__\-__ static/  
__--__ img/  
__--__ js/  
__--__ css/  
__\-__ default/ _(default blueprint)_  
__--__ \_\_init\_\_.py _(defines blueprint name and calls the routes)_   
__--__ routes.py   
__--__ forms.py _(form models for this blueprint)_  
__\-__ \_\_init\_\_.py _(function to register blueprints, initialize extensions and bootstrap the application)_  
__\-__ models.py  
config.py  _(config mostly set via envrionment variables. no configuration tweaking needed for development)_  
manage.py  _(call flask-script to handle our commad line interface)_