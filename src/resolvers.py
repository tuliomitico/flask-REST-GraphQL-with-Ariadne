from ariadne import load_schema_from_path, QueryType, MutationType, make_executable_schema

from .modules.users.services.get_users_service import GetUserService
from .modules.users.services.create_user_service import CreateUserService
from .modules.posts.services.create_post_service import CreatePostService
from .modules.posts.services.get_user_by_post_service import GetUserByPostService

type_defs = load_schema_from_path('./src/modules')
query = QueryType()
mutation = MutationType()

@query.field('resolve_users')
def resolve_users(_,info):
    return GetUserService().execute()

@query.field('resolve_posts')
def resolve_posts(_,info,id):
    return GetUserByPostService().execute(id=id)

@mutation.field('create_user')
def create_user(_,info,input: dict):
    return CreateUserService().execute(input['name'],input['username'])

@mutation.field('create_post')
def create_post(_,info,input: dict):
    return CreatePostService().execute(input['content'],input['author'])

@query.field("hello")
def resolve_hello(_,info):
    request = info.context
    user_agent = request.headers.get('User-Agent','Guest')
    return "Hello, %s!" % user_agent

schema = make_executable_schema(type_defs,query,mutation)