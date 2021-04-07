# `Contacts Management Flask APIs`
Is a Flask web based API project.

### How to run the project
Run the following command to do so:
* Clone the project from git on your system
* cd `contacts-management-flask-apis`
* Create a virtual environment and activate it
* Install site-packages by using following command: `pip install requirements.txt` 
* Run `python manage.py db init` to initiate migrations. It will create a directory named "migrations"
* Run `python manage.py db upgrade` to apply the migrations to the database.
* Run `python manage.py run` to execute the flask app server.

### How to run tests
* Run `python mange.py test`
