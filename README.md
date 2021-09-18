# django-0auth

>Django Authentication backend web APIs - Auth0.


### Prerequisites
###### Prerequisites

- Python 3.8.5
- Psql 13.0

The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

```bash
git clone https://github.com/mbrsagor/django-0auth.git
cd django-0auth
virtualenv venv --python=python3.8
source venv/bin/activate
```
Then create `.env` file and paste code from `example.env` file and add validate information.
###### After that run the server in development or production environment

###### Multiple database configurations:
```python
DATABASES = {
    'default': {},
    'users': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "users_mydb",
        'USER': "mbr-sagor",
        'PASSWORD': "123456",
    },
    'listing': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "users_mydb",
        'USER': "mbr-sagor",
        'PASSWORD': "123456",
    },
    'HOST': "localhost",
    'PORT': 5432,
}
```

##### Migrate User database related commands:
```bash
./manage.py migrate user --database=users
./manage.py createsuperuser --database=users
```
