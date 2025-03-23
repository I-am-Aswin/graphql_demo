from flask import request, jsonify
from ariadne.explorer import ExplorerGraphiQL
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType

from api import app
from api.queries import listposts_resolver, getpost_resolver
from api.mutations import createpost_resolver, updatepost_resolver, deletepost_resolver
# from api import models

query = ObjectType("Query")
query.set_field('hello', lambda obj, info : "Hello World")
query.set_field('listPosts', listposts_resolver)
query.set_field('getPost', getpost_resolver)

mutation = ObjectType("Mutation")
mutation.set_field('createPost', createpost_resolver)
mutation.set_field('updatePost', updatepost_resolver)
mutation.set_field('deletePost', deletepost_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def playground():
    """ GraphQL Playground """
    return ExplorerGraphiQL().html(None)

@app.route("/graphql", methods=["POST"])
def graphql_server():
    """ GraphQL Server """
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
