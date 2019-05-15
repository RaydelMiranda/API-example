# Persons.

This is a simple project for illustrating the implementation of a simple API. It also contains a couple of test cases implemented using PyTest.

Skills:

1. Testing (TDD).
2. Version control.
3. Python.
4. Django.
5. Django REST Framework.
6. Internationalization

## Running the API.

In order to run/test the API, while in the project root folder follow the next steps:

1. Create a python virtual environment. (https://virtualenvwrapper.readthedocs.io/en/latest/)
2. Install project requirements.
    
    a. activate virtual environment.
   
    b. pip install -r requirements.txt

3. Create migrations (./manage.py createmigrations)

4. Migrate (./manage.py migrate)    

5. Run the server (./manage.py runserver)

The last step will run a development server which can be accessed with the URL  http://127.0.0.1:8000 

## Runing Tests

Follow steps 1 and 2 from the section "Running the API". navigate into the tests folder and just run:

$ pytest  