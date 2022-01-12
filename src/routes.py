from ariadne import ( graphql_sync )
from ariadne.constants import PLAYGROUND_HTML
from flask import Blueprint, jsonify, request, current_app
from flask.views import MethodView
from flask_smorest import Blueprint as BlueSmorest
from http import HTTPStatus

from .modules.users.controllers.create_user_controller import CreateUserController
from .modules.posts.controllers.get_user_by_post_controller import GetUserByPostController
from .models.post import Post
from .schemas.post import PostSchema, UserSchema
from .resolvers import schema

blp = BlueSmorest('index',__name__,description="Operation in Posts and Users")
blp_gql = Blueprint('graphql',__name__)

@blp.route('/posts/user/<int:id>')
class Posts(MethodView):
    @blp.response(200,schema=PostSchema)
    def get(self,id):
        """Get posts by user id"""
        return GetUserByPostController().handle(id)

@blp.route('/users',endpoint='create_user')
class User(MethodView):
    @blp.response(201,schema=UserSchema)
    @blp.alt_response(201,schema_or_ref=None,description="The user already exists")
    @blp.arguments(schema=UserSchema)
    def post(self,new_data):
        """Create a user"""
        return CreateUserController().handle()

@blp.route('/')
@blp.response(200,example={"message":"Hello World!"})
def index():
    return {'message':'Hello World!'}

@blp.route('/posts')
def get_posts_by_user():
    post_query = Post.query.all()
    posts = PostSchema(many=True)
    return jsonify(data=posts.dump(post_query))

@blp_gql.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=current_app.debug
    )

    status_code = HTTPStatus.OK if success else HTTPStatus.BAD_REQUEST
    return jsonify(result), status_code

@blp_gql.route("/graphql", methods=["GET"])
def graphql_playground():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, HTTPStatus.OK