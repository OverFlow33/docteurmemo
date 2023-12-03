=====
Docteurmemo Database Objects
=====

The Docteurmemo Database Objects Python package is a robust and versatile solution for managing 
healthcare-related data in a database. It offers a set of classes and methods to seamlessly 
interact with and manipulate information about Patients, Caregivers, and HealthcareProfessionals. 
This package simplifies database transactions, making it an ideal choice for healthcare applications and systems.


Quick start
-----------

1. Add "database_objects" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "database_objects",
    ]

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).