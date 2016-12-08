# Reviewit

## How to run this app (Docker)

To run this project you need to have Docker installed, you can get it from [here](https://www.docker.com/products/docker/)

Documentation about Docker can be found [here](https://docs.docker.com/)

Check you have docker installed and running by running this command `docker info`

If you get this message:

*[Error response from daemon: Bad response from Docker engine]*

docker is not running.

If not, go inside the project and run `docker-compose -f docker-compose-prod.yml up`
The first time will take a while, docker is downloading everything he needs to run the project, be patient.

## How to hit the endpoints
**Create a user**

`curl -X POST -d "username={username}&password={password}&email={email}" http://127.0.0.1/core/users/`


**Get this user token**

`curl -X POST -d "username={username}&password={password}" http://127.0.0.1/api-token-auth/`


**Post some reviews**

`curl -H 'Authorization: Token {token}' -X POST -d "company={company_id}&title={title}&summary={summary}&rating={rating}" http://127.0.0.1:8000/reviews/list/`


**Retrieve reviews**

`curl -H 'Authorization: Token {token}' -X GET http://127.0.0.1/reviews/list/`

## Runnning tests

`docker exec -it reviewer_web_prod_1 python manage.py test --settings=reviewer.test`

## Checking the admin interface

When docker is first runned a superuser is created (only if there is no other) you can access

the admin site with this credentials:

```
username: admin
password: AdminPWD
```
