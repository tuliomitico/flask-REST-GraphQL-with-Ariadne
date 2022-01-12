from src.models.user import User

class CreateUserService:
    def execute(self,name,username):
        user_already_exists = User.query.filter_by(name=name).first()

        if user_already_exists:
            raise Exception("User already exists")

        user = User(name,username).create()
        return user
