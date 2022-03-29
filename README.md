# URL Shortener

## Instructions
In this folder run:
```
docker-compose up
```
Go to: http://localhost:8000

## Tests
Make sure the server is running and run the following:
```
docker exec -it $(docker ps | grep url-shortener-web | awk '{ print $1 }') python manage.py test
```

## Uses
[Halfmoon](https://www.gethalfmoon.com/)