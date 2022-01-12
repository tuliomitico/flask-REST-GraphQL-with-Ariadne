from src.models.user import User

class GetUserService:
    def execute(self):
        users  = User.query.all()

        return users
