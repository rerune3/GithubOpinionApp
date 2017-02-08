from opinion_proto import Opinion
from opinion_proto import OpinionComment

class BackendHelper(object):

    @staticmethod
    def opinion_model_to_proto(opinion_model):
        return Opinion(author=opinion_model.Author,
            tags=opinion_model.Tags, text=opinion_model.Text,
            likes=opinion_model.Likes, dislikes=opinion_model.Dislikes,
            timestamp_sec=opinion_model.OpinionTimestampSec,
            opinion_id=opinion_model.OpinionID)

    @staticmethod
    def comment_model_to_proto(comment_model):
        return OpinionComment(author=comment_model.Author,
            text=comment_model.Text, likes=comment_model.Likes,
            dislikes=comment_model.Dislikes,
            timestamp_sec=comment_model.CommentTimestampSec,
            opinion_id=comment_model.OpinionID,
            comment_id=comment_model.CommentID)

    @staticmethod
    def opinion_model_results_to_proto_list(opinion_model_results):
        arr = []
        for opinion in opinion_model_results:
            arr.append(BackendHelper.opinion_model_to_proto(opinion))
        return arr

    @staticmethod
    def comment_model_results_to_proto_list(comment_model_results):
        arr = []
        for comment in comment_model_results:
            arr.append(BackendHelper.comment_model_to_proto(comment))
        return arr
