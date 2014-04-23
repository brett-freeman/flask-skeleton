flask-skeleton
==============

A simple skeleton for quickly setting up a flask app. Utilizes blueprints for views and flask-sqlalchemy for the ORM

All package dependencies needed to get up and running are included in requirements.txt

Version 2.0 now uses blueprints in place of flask-classy, as well as highly improved structure.

Blueprint provided is named 'default' and is a simple placeholder for you to build from.

SQLAlchemy will default to a sqlite database stored in the root of the application failing the environment variables outlined in config.py are not set.

Secret key is set by environment variable as well._

app/
- templates/
-- default/
--- index.html
-- base.html
- static/
-- img/
-- js/
-- css/
- default/
-- __init__.py
-- routes.py
-- forms.py
- __init__.py
- models.py
config.py
manage.py

