# WePost

## Prerequist

* python3.7

## Deployment
To deploy this project on your device, please 
```
    pip install -r requirements.txt
    python manage.py makemigrations signuser wepost_main
    python manage.py migrate
    python populate_script.py
    python manage.py runserver
```

## Tests

it is not recommended to run the tests file, because the populate script contains way too much information of users and posts which makes every execution of `populate()` cost a long time.