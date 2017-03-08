BarnAuction
===========

ActonBarn Auction



Setup:
------ First step: set up virtual environment ----
Read this for more information:
http://docs.python-guide.org/en/latest/dev/virtualenvs/

Step by step:

1. pip install virtualenv
2. virtualenv -p /usr/bin/python2.7 venv
3. source venv/bin/activate
4. pip install -r requirements.txt
--------------------------------------
Then set up the app

5. python manage.py syncdb # to initialize the db 
6. python manage.py runserver # to lunch the service

