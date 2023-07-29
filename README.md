All files in the project folder is explained here:

Updated by Madhumitha Jayakumar at 8.14 PM 29-07-2023

manage.py -
This is the executer to pull DB tables and populate the models.py as classes.
To achieve this, need to run this command -> python manage.py inspectdb > models.py

models.py -
This is the file that contains all the DB tables as classes. This is the basic concept of
Django ORM, where CRUD is performed on DB tables.

./online_store/views -
This is where the main logic of the online store is located. It contains multiple 
APIs that are called by frontend based on the user access privilege.

DB_Schema.sql -
This is the schema for entire DB created for this online store. Excecute this query file
to create the entire DB.