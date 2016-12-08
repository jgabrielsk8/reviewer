# reviewit

## How to run this app (Docker)

To run this project you need to have Docker installed, you can get it from [here](https://www.docker.com/products/docker/)

Documentation about Docker can be found [here](https://docs.docker.com/)

Check you have docker installed and running by running this command `docker info`

If you get this message docker

*[Error response from daemon: Bad response from Docker engine]*

is not running.

If not go inside the project and run `docker-compose -f docker-compose-prod.yml up`
## How to hit the endpoints

`curl -X POST -d "username={username}&password={password}&email={email}" http://127.0.0.1/core/users/`

`curl -X POST -d "username={username}&password={password}" http://127.0.0.1/api-token-auth/`

`curl -H 'Authorization: Token {token}' -X POST -d "company={company_id}&title={title}&summary={summary}&rating={rating}" http://127.0.0.1:8000/reviews/list/`

`curl -H 'Authorization: Token {token}' -X GET http://127.0.0.1/reviews/list/`

## Runnning tests

`docker exec -it reviewer_web_prod_1 python manage.py test --settings=reviewer.test`


