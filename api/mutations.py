from ariadne import convert_kwargs_to_snake_case
from .models import Post
from . import db

@convert_kwargs_to_snake_case
def createpost_resolver(obj, info, title, description):

    try :
        post = Post( 
            title = title, 
            description = description
        )

        db.session.add(post)
        db.session.commit()

        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError as err :
        payload = {
            "success": False,
            "error": [str(err)]
        }
    
    return payload


@convert_kwargs_to_snake_case
def updatepost_resolver(obj, info, id, title, description):

    try:
        post = Post.query.get(id)

        if( title is not None ):
            post.title = title
        
        if( description is not None ):
            post.description = description
        
        db.session.add(post)
        db.session.commit()

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

@convert_kwargs_to_snake_case
def deletepost_resolver(obj, info, id):

    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()

        payload = {
            "success": True,
            "post": post.to_dict()
        }
    
    except AttributeError as err:
        payload = {
            "success": False,
            "post": [str(err)]
        }
    
    return payload
