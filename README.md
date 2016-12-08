# reviewit

## How to run this app (Docker)

## How to hit the endpoints

curl -X POST -d "username={username}&password={password}&email={email}" http://127.0.0.1:8000/core/users/
curl -X POST -d "username={username}&password={password}" http://127.0.0.1:8000/api-token-auth/
curl -H 'Authorization: Token {token}' -X POST -d "company={company_id}&title={title}&summary={summary}&rating={rating}" http://127.0.0.1:8000/reviews/list/
curl -H 'Authorization: Token {token}' -X GET http://127.0.0.1:8000/reviews/list/

## Runnning tests

python manage.py test --settings=reviewer.test


