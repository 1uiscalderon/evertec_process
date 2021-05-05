# Evertec

## Description

    This is a light app created with Django that uses simulates the creation and payments
    of orders of a small store

## Content

- [apiStore](./apiStore/settings): Project settings
- [app_v1](./app_v1): App of the project that holds models, urls, tests, static content, etc.

## Requirements

- Django
- Python 3.6
- mySQL
- Ubuntu 18.04

## Usage

You can clone this repository and install all the requierements

    git clone https://github.com/1uiscalderon/evertec_process.git

## Getting started

To install the requirements just type in your terminal:

    -pip install -r requirements.txt or pip3

I used mySQL as database engine, so make sure you have installed this program and create a table
called "api_store", you can either create this table or change this name in settings.

In the .env file are stored mostly credentials such as database user, database password, LOGIN and
TRAN_KEY, please have that in mind.

After creating a virtual env and installing django , run the program command python3 manage.py runserver

in this URL(http://localhost:8000/store/) the user will find the main page which is the list of all orders.

Next to the StoreApp sign are 2 links Orders and Add Order.

The fisrt one will return the user to the main page the second one will show a form to create a new order.
it requieres 3 field: 
    - Name: Full name
    - Email: requieres @
    - Mobile

Once the form is done, by clicking submit a new window will show the ordir ID along with 2 buttons.
    - See Orders: returns to the main page
    - See order Now: Show all the fields inside the order created

Lastly there is a search field to introduce a valid Order id, if it is a valid id, it will redirect the user
to the order details, otherwise will show error.

## Bugs

Currently this app is not redirecting to placetopay to validate the payment.
