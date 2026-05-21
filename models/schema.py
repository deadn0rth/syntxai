USER_SCHEMA = {
    "id": int,
    "name": str,
    "email": str,
}

POST_SCHEMA = {
    "id": int,
    "title": str,
    "body": str,
    "userId": int,
}

COMMENT_SCHEMA = {
    "id": int,
    "postId": int,
    "name": str,
    "email": str,
    "body": str,
}
