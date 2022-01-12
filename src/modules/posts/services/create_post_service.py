from src.models.post import Post
from src.models.user import User

class CreatePostService:
    def execute(self,content,author):
        post = Post(content=content,author_id=author).create()
        return post