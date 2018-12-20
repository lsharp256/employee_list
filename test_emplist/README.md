This app stores employee information in a table 
and can be sorted by clicking on the different table
headers (First Name, Last Name, Date Started).

**How to use app:**

Create a psql database called '**employee_list_database**'.

'`createdb employee_list_database`'

After connecting to the database, install 'requirements.txt'
with '`pip install -r requirements.txt`'

Navigate to employee_list folder and 
run the following commands:

`python manage.py migrate`

`python manage.py runserver`

Navigate to 127.0.0.1:8000 in the browser to view app.

Please note: The Date started field accepts the data in the following
 format: `YYYY-MM-DD HH:MM`