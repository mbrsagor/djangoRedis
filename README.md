# django-0auth

>Django Authentication backend web APIs - Auth0.


### Prerequisites
###### Prerequisites

- Python 3.8.5
- Django
- Django Rest Framework

The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

```bash
git clone https://github.com/mbrsagor/django-0auth.git
cd django-0auth
virtualenv venv --python=python3.8
source venv/bin/activate
```
Then create `.env` file and paste code from `example.env` file and add validate information.
###### After that run the server in development or production environment

```bash
./manage.py migrate
./manage.py runserver
```

https://auth0.com/blog/django-authentication/
