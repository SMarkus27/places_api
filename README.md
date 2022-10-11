## A Simple DJANGO REST API

A simple API to manage places (CRUD). This API allow to:

* Create a place
* Edit a place
* Get a specific place
* Delete a specific place

A place must have the following fields:

```
{
  "name":"str",
  "slug":"str",
  "city":"str",
  "state":"str"
}
```

## How to run the API

* Clone the repo
* Run the following command in terminal:

```
pip install requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```

## Using the Postman

* GET all places

```
http://127.0.0.1:8000/api/v1/places/

```
* GET a specific place

```
http://127.0.0.1:8000/api/v1/places/

```

* POST the places

```
http://127.0.0.1:8000/api/v1/places/

```

* PUT the places

```
http://127.0.0.1:8000/api/v1/places/id

```
* DELETE the places

```
http://127.0.0.1:8000/api/v1/places/id

```

