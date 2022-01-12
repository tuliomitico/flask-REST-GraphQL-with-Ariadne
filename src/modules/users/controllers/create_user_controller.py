from flask import request
from flask.json import jsonify
from http import HTTPStatus

from src.schemas.post import UserSchema

from ..services.create_user_service import CreateUserService

class CreateUserController:

    def handle(self):
        data = request.get_json()
        try:
            user = CreateUserService().execute(data['name'],data['username'])
        except Exception as e:
            return jsonify(error=str(e)), HTTPStatus.BAD_REQUEST
        user_schema=UserSchema(load_instance=True)
        return jsonify(data=user_schema.dump(user)),HTTPStatus.CREATED