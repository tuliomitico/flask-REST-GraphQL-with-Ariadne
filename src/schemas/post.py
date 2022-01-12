from marshmallow_sqlalchemy import fields
from .schemas import ma

from ..models.user import User
from ..models.post import Post

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field()
    username = ma.auto_field()


class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Post
        fields = ['_id','content','author','author_id']
        include_fk = True
    author = fields.Nested(UserSchema)
