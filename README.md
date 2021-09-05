# RestApi-mongoDB
Implement a shopping cart using Django REST Framework and MongoDB as the backend

# Problem Statement
To create a shopping cart REST API(Use Python/Mongodb) that handles CRUD operations for a specific user like create cart, get items, add items and remove items.

# Solution
## Tools  Required
- MongoDB : To create and maintain database
- Postman App/ Insomnia : To make requests to API from client side
- Python(3.9.6) : To create the API

## Download and Install Required  tools
- MongoDB Community Version (5.0.1) : https://www.mongodb.com/try/download/community
- Postman : https://www.postman.com/downloads/
- Python (3.9.6) : https://www.python.org/downloads/

## Required  packages for python
- Django : To work with Django framework in python
- Djongo : Django ORM framework to work with MongoDB in Django
- Django-rest-framework : To create rest api using django

##### Command to  install required packages
- All  packages at once : pip install -r requirements.txt
- Individual packages : pip install <package_name> 
  - <package_name> : django, djongo, django-rest-framework

## Operations that can be performed with API
- Create and/or Add items to  cart
- Get items in cart
- Update name for  item in  cart
- Update price for item in cart
- Update quantity for  item in cart
- Remove specific item from cart
- Empty cart

## Instructions to get this working
- make a virtual environment and install all the python packages using the following commands
    - pip install virtualenv
    - virtualenv env
    - for LINUX/MAC os : source myvenv/bin/activate
    - for WINDOWS : env\Scripts\activate.bat
    - pip install -r requirement.txt
- install mongoDB and make a local database with the name "cart_database"
- Activate the virtual enviroment and write the following commands
    - python3 manage.py migrate
    - python3 manage.py runserver
- After the server is running use postman/insomnia to sent requests
- send GET, POST request to localhost:port/cart/ to get details of the cart and add item to the cart
- send PUT, DELETE, PATCH request to localhost:port/cart/<id> to update/partially update/delete the item in the cart 
