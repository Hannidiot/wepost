# WePost

## Prerequist

* python3.7

## Deployment
To deploy this project on your device, please 
```
    pip install -r requirements
    python manage.py makemigrations signuser wepost_main
    python manage.py migrate
    python populate_script.py
    python manage.py runserver
```