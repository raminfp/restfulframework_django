# restful_django

## Setup

```shell
pip install -r requirements.txt
```

```shell
python manage.py makemigrations; python manage.py migrate
```

```shell
python manage.py runserver
```


## GET 

```shell
curl http://localhost:8000/
```

## POST

```shell
curl -X POST http://localhost:8000/ -d "firstname=ramin world&lastname=Farajpour&email=ramin@blackhat.gmail.com&address=bandapiiii"
```

## PUT

```shell
curl -X PUT http://127.0.0.1:8000/update/1 -d "firstname=mostafa&lastname=mami&email=blackhat@gmail.com&address=iran"
```

## DELETE 

```shell
curl -X DELETE http://127.0.0.1:8000/delete/1
```

## TODO

- [ ] New features
