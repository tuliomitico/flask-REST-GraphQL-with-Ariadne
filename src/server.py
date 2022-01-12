import typing

from flask import Flask
from flask_smorest import Api
from sqlalchemy.exc import IntegrityError


from .models.user import User
from .models.post import Post
from .database.db import db
from .schemas.schemas import ma
from .routes import blp, blp_gql

def setup_app(app: Flask):
    @app.before_first_request
    def create_db():
        db.create_all()
        try:
            user = User(name='Jorge',username='cloroquina')
            post = Post(content='Test',author_id=4,author=None)
            db.session.add(user)
            db.session.add(post)
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
    api = Api()
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    api.register_blueprint(blp)

def create_app(test_config: typing.Union[str,typing.Dict[str,typing.Any],None] = None):
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'str'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
    app.config['API_TITLE'] = 'Flask GraphQl REST API'
    app.config['API_VERSION'] = '1.0.0'
    app.config['OPENAPI_VERSION'] = '3.0.2'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_RAPIDOC_PATH'] = '/rapidoc'
    app.config['OPENAPI_RAPIDOC_URL'] = 'https://cdn.jsdelivr.net/npm/rapidoc/dist/rapidoc-min.js'

    setup_app(app)
    app.register_blueprint(blp_gql)
    return app