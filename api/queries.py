from ariadne import convert_kwargs_to_snake_case
from .models import Post
from . import db

def listposts_resolver(obj, info):

    try :
        posts = [ post.to_dict() for post in Post.query.all() ]

        payload = {
            "success": True,
            "post": posts
        }
    
    except Exception as err:

        payload = {
            "success": False,
            "error": [str(err)]
        }

    return payload

@convert_kwargs_to_snake_case
def getpost_resolver(obj, info, id):

    try:
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError as err:
        payload = {
            "success": False,
            "error": [str(err)]
        }
    return payload