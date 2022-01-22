# djangoRedis

>Uses native redis-py url notation connection strings like, Pluggable clients, Pluggable parsers, Highly configurable, and etc.


### Setup
###### Prerequisites

- Python 3.8.5
- Redis

The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

```bash
git clone https://github.com/mbrsagor/djangoRedis.git
cd djangoRedis
virtualenv venv --python=python3.8
source venv/bin/activate
```
Then create `.env` file and paste code from `example.env` file and add validate information.
###### After that run the server in development or production environment

###### Run the development server:
```bash
./manage.py makemigrations
./manage.py createsuperuser
./manage.py runserver
```

###### Configure as cache backend.
```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```


##### Open Redis CLI: ```redis-cli```
> Input:      
```redis-cli   
127.0.0.1:6379> set a 100
OK
```
> Output:
```redis-cli 
127.0.0.1:6379> get a
"100"
127.0.0.1:6379> 
```
