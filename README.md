Overview
This project is a sample for Task Management API using Python, Flask ,SQLAlchemy for back-end development and postgreSQL as database.

Purpose
The Objective for this task is to create RESTful apis allowing the user to handle task management.

Technologies
The technologies used in this Sample are:
- Python flask application
- SQLAlchemy
- PostgreSQL
- psycopg2

Requirements
For the requirements the following libraries are needed:
- alembic==1.11.1
- anyio==3.7.1
- blinker==1.6.2
- certifi==2023.5.7
- click==8.1.6
- colorama==0.4.6
- dnspython==2.4.0
- email-validator==1.1.2
- Flask==2.3.2
- Flask-Migrate==4.0.4
- Flask-SQLAlchemy==3.0.5
- Flask-Validator==1.4.2
- Flask-WTF==1.1.1
- greenlet==2.0.2
- h11==0.14.0
- httpcore==0.17.3
- idna==3.4
- isbnlib==3.10.3
- iso3166==1.0.1
- itsdangerous==2.1.2
- Jinja2==3.1.2
- Mako==1.2.4
- MarkupSafe==2.1.3
- psycopg2==2.9.6
- psycopg2-binary==2.9.6
- py-moneyed==0.8.0
- pycountry==22.3.5
- python-dotenv==1.0.0
- pytz==2020.1
- schwifty==2020.9.0
- sniffio==1.3.0
- SQLAlchemy==1.4.46
- typing_extensions==4.7.1
- waitress==2.1.2
- Werkzeug==2.3.6
- WTForms==3.0.1

Set Up:
Create a database in postgreSQL named NeoDB , while adding a new table called task where the fields are :
- ID (Serial, Primary Key, Not Null and Unique)
- title (text)
- description (text)
- completed (boolean)
For the database connection in the .env file change the following url in DEVELOPMENT_DATABASE_URL to:
- your database info in this format 'postgresql+psycopg2://user:password@localhost:port/DataBaseName'