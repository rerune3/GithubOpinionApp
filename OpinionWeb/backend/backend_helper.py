from proto import Post
from proto import Comment

class BackendHelper(object):

    @staticmethod
    def post_model_to_proto(post_model):
        return Post(author=post_model.Author,
            tags=post_model.Tags, text=post_model.Text,
            likes=post_model.Likes, dislikes=post_model.Dislikes,
            timestamp_sec=post_model.PostTimestampSec,
            post_id=post_model.PostID)

    @staticmethod
    def comment_model_to_proto(comment_model):
        return Comment(author=comment_model.Author,
            text=comment_model.Text, likes=comment_model.Likes,
            dislikes=comment_model.Dislikes,
            timestamp_sec=comment_model.CommentTimestampSec,
            post_id=comment_model.PostID,
            comment_id=comment_model.CommentID)

    @staticmethod
    def post_model_results_to_proto_list(post_model_results):
        arr = []
        for post in post_model_results:
            arr.append(BackendHelper.post_model_to_proto(post))
        return arr

    @staticmethod
    def comment_model_results_to_proto_list(comment_model_results):
        arr = []
        for comment in comment_model_results:
            arr.append(BackendHelper.comment_model_to_proto(comment))
        return arr
