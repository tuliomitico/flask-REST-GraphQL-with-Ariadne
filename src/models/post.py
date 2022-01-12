import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_utils.models import Timestamp

from .user import User

from ..database.db import db

class Post(db.Model,Timestamp):
    _id = sa.Column('id',sa.Integer,primary_key=True)
    content = sa.Column(sa.Text)
    author = orm.relationship('User')
    author_id = sa.Column(sa.Integer,sa.ForeignKey('user.id',ondelete='CASCADE'))

    def __init__(self,content: str,author_id:int, **kwargs,) -> None:
        super(Post,self).__init__(**kwargs)
        self.content = content
        # self.author = author
        self.author_id = author_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self