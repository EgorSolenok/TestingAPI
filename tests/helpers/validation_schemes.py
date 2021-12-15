

class PostsScheme:
    SCHEME = {
        "userId": {'type': 'number'},
        "id": {'type': 'number'},
        "title": {'type': 'string'},
        "body": {'type': 'string'}
    }

    PATCH_SCHEME = {
        "userId": {'type': 'number'},
        "id": {'type': 'number'},
        "title": {'type': 'string'},
        "body": {'type': 'string'}
    }

    PUT_SCHEME = {
        "body": {'type': 'string'},
        "id": {'type': 'number'}
    }

class CommentsScheme:
    SCHEME = {
        "postId": {'type': 'number'},
        "id": {'type': 'number'},
        "name": {'type': 'string'},
        "email": {'type': 'string'},
        "body": {'type': 'string'}
    }
