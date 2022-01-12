from flask.json import jsonify
from http import HTTPStatus

from src.schemas.post import PostSchema

from ..services.get_user_by_post_service import GetUserByPostService

class GetUserByPostController:

    def handle(self,id):
        post = GetUserByPostService().execute(id)
        post_schema=PostSchema(many=True)
        return jsonify(data=post_schema.dump(post)),HTTPStatus.OK