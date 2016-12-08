# reviewit

curl -X POST -d "username=user1&password=Test123456&email=user1@mail.com" http://127.0.0.1:8000/core/users/
curl -X POST -d "username=user1&password=Test123456" http://127.0.0.1:8000/api-token-auth/
curl -H 'Authorization: Token d2fda312232fecda11e15924f10a280a79837ee7' -X POST -d "company=2&title=Testing first review&summary=this is a test&rating=5" http://127.0.0.1:8000/reviews/list/
curl -H 'Authorization: Token d2fda312232fecda11e15924f10a280a79837ee7' -X GET http://127.0.0.1:8000/reviews/list/