import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy_utils.models import Timestamp

from ..database.db import db

class User(db.Model,Timestamp):
    id = sa.Column(sa.Integer,primary_key=True)
    name = sa.Column(sa.Text,unique=True)
    username = sa.Column(sa.Text)
    def __init__(self,name: str,username: str,**kwargs) -> None:
        super(User,self).__init__(**kwargs)
        self.name = name
        self.username = username
        
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self