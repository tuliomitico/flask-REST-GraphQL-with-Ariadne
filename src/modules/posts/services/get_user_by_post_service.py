from src.models.post import Post
from src.schemas.post import PostSchema

class GetUserByPostService:
    def execute(self,id):
        post = Post.query.filter_by(author_id=id).all()
        post_schema = PostSchema(many=True)
        return post_schema.dump(post)