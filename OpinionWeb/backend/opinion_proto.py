from protorpc import messages

class OpinionComment(messages.Message):
    author = messages.StringField(1, required=True)
    text = messages.StringField(2, required=True)
    likes = messages.IntegerField(3, required=False)
    dislikes = messages.IntegerField(4, required=False)
    timestamp_sec = messages.IntegerField(5, required=True)
    opinion_id = messages.StringField(6, required=True)
    comment_id = messages.StringField(7, required=True)

class Opinion(messages.Message):
    author = messages.StringField(1, required=True)
    tags = messages.StringField(2, repeated=True)
    text = messages.StringField(3, required=True)
    likes = messages.IntegerField(4, required=False)
    dislikes = messages.IntegerField(5, required=False)
    timestamp_sec = messages.IntegerField(6, required=True)
    opinion_id = messages.StringField(7, required=True)

class OpinionList(messages.Message):
    opinion_list = messages.MessageField(Opinion, 1, repeated=True)

class CommentList(messages.Message):
    comment_list = messages.MessageField(OpinionComment, 1, repeated=True)

class OpinionListRequest(messages.Message):
    # How many posts to retrieve.
    size = messages.IntegerField(1, required=False)
    tags = messages.StringField(2, repeated=True)

class CommentListRequest(messages.Message):
    opinion_id = messages.StringField(1, required=True)
    size = messages.IntegerField(2, required=False)

class CommentWorkRequest(messages.Message):
    comment_id = messages.StringField(1, required=False)

class OpinionWorkRequest(messages.Message):
    opinion_id = messages.StringField(1, required=False)

class RequestFeedback(messages.Message):
    # Should be set using AppErrors.
    status = messages.IntegerField(1, required=True)
    error_message = messages.StringField(2, required=True)

class OpinionBundle(messages.Message):
    opinion = messages.MessageField(Opinion, 1, required=False)
    comments = messages.MessageField(OpinionComment, 2, repeated=True)
