# Cloud-Finantial-Structure

![Current Version](https://img.shields.io/badge/version-v0.1-blue)
![GitHub contributors](https://img.shields.io/github/contributors/madhur-taneja/README-Template)

## Table of Contents
- [Getting Started](#getting-started)
	- [Tools Required](#tools-required)
	- [Installation](#installation)
	- [Structure](#struture)
	- [Use](#use)

## Getting Started

### Tools Required

* Python 3.9
* Django 4.2
* djangorestframework 3.14
* celery 5.2
* django-celery-beat 2.5
* redis 4.5

### Installation

All installation steps go here.

After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command:
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`subscription` | GET | READ | Get all subscriptions of the customer
`invoice` | GET | READ | Get all invoices of the customer
`subscription`| POST | CREATE | Create a new subscriptions for the customer
`invoicehistory` | GET | READ | Get number of all the customer invoices and the customer cost
`activate/:id` | PUT | UPDATE | Activate a subscription
`deactivate/:id` | PUT | UPDATE | Deactivate a subscription

## Use

In first terminal, we have to start up Django's development server:
```bash
python manage.py runserver
```
In second terminal, we run the broker server:
```bash
redis-server
```
In Third terminal, we run the scheduler:
```bash
celery -A celeryapp beat -l info
```
In Fourth terminal, we run the Celery worker:
```bash
celery -A celeryapp worker -l info
```

Now we should open [admin](http://127.0.0.1:8000/admin/) interface of our project in the browser and create a customer.Then we can create a token for required authorization.
We can test the API using [Postman](https://www.postman.com/), first we should set Authorization Key to toke for each api test as below:

![plot](./images/1.png)

Now we test apis:

1.POST method of subscription api:

![plot](./images/POST_subscription.png)

2.GET method of subscription api:

![plot](./images/GET_subscription.png)

3.GET method of invoice api:

![plot](./images/invoce.png)

4.GET method of invoicehistory api:

![plot](./images/invoicehistory.png)

5.PUT method of activate api:

![plot](./images/activate.png)

6.PUT method of deactivate api:

![plot](./images/deactivate.png)



[//]: # (HyperLinks)

[GitHub Repository]: https://github.com/madhur-taneja/README-Template
[GitHub Pages]: https://madhur-taneja.github.io/README-Template
[CONTRIBUTING.md]: https://github.com/madhur-taneja/README-template/blob/master/CONTRIBUTING.md
[tags]: https://github.com/madhur-taneja/README-template/tags

[GitHub]: https://github.com/mohsenkk
[LinkedIn]: https://www.linkedin.com/in/madhur-taneja/

[contributors]: https://github.com/madhur-taneja/README-template/contributors
[license]: https://github.com/madhur-taneja/README-template/blob/master/LICENSE.md
