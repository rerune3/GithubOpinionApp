from protorpc import messages

class Comment(messages.Message):
    author = messages.StringField(1, required=True)
    text = messages.StringField(2, required=True)
    likes = messages.IntegerField(3, required=False)
    dislikes = messages.IntegerField(4, required=False)
    timestamp_sec = messages.IntegerField(5, required=True)
    post_id = messages.StringField(6, required=True)
    comment_id = messages.StringField(7, required=True)

class Post(messages.Message):
    author = messages.StringField(1, required=True)
    tags = messages.StringField(2, repeated=True)
    text = messages.StringField(3, required=True)
    likes = messages.IntegerField(4, required=False)
    dislikes = messages.IntegerField(5, required=False)
    timestamp_sec = messages.IntegerField(6, required=True)
    post_id = messages.StringField(7, required=True)

class PostListResponse(messages.Message):
    post_list = messages.MessageField(Post, 1, repeated=True)

class CommentListResponse(messages.Message):
    comment_list = messages.MessageField(Comment, 1, repeated=True)

class PostListRequest(messages.Message):
    # How many posts to retrieve.
    size = messages.IntegerField(1, required=False)
    tags = messages.StringField(2, repeated=True)

class CommentListRequest(messages.Message):
    post_id = messages.StringField(1, required=True)
    size = messages.IntegerField(2, required=False)

class CommentWorkRequest(messages.Message):
    comment_id = messages.StringField(1, required=False)

class PostWorkRequest(messages.Message):
    post_id = messages.StringField(1, required=False)

class RequestFeedback(messages.Message):
    # Should be set using AppErrors.
    status = messages.IntegerField(1, required=True)
    error_message = messages.StringField(2, required=True)
    unique_id = messages.StringField(3, required=False)

class PostBundle(messages.Message):
    post = messages.MessageField(Post, 1, required=False)
    comments = messages.MessageField(Comment, 2, repeated=True)
