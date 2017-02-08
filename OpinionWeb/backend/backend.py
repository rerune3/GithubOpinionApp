from google.appengine.ext import endpoints
from google.appengine.ext import ndb
from protorpc import message_types
from protorpc import remote

from app_errors import AppErrors

from backend_helper import BackendHelper
from backend_query import OpinionQuery

from opinion_models import OpinionModel
from opinion_models import OpinionCommentModel

from opinion_proto import CommentList
from opinion_proto import CommentListRequest
from opinion_proto import CommentWorkRequest
from opinion_proto import OpinionWorkRequest
from opinion_proto import OpinionListRequest
from opinion_proto import OpinionBundle
from opinion_proto import Opinion
from opinion_proto import OpinionComment
from opinion_proto import OpinionList
from opinion_proto import RequestFeedback

from uuid import uuid4

@endpoints.api(name='opinions', version='v1', description='API for Opinions')
class OpinionAPI(remote.Service):

    @endpoints.method(Opinion, RequestFeedback,
                        name='insert_new_opinion',
                        path='app.insert_new_opinion',
                        http_method='POST')
    def insert_new_opinion(self, request):
        if OpinionQuery.opinion_in_datastore(request.opinion_id):
            return RequestFeedback(status=AppErrors.ID_ALREADY_EXISTS,
                error_message=('Opinion post with ID %s already exists. awk..')
                                % (request.opinion_id))

        OpinionModel(Author=request.author, Tags=request.tags,
                    Text=request.text, Likes=request.likes,
                    Dislikes=request.dislikes,
                    OpinionTimestampSec=request.timestamp_sec,
                    OpinionID=request.opinion_id,
                    id=request.opinion_id).put()

        return RequestFeedback(status=AppErrors.NO_ERRORS,
                    error_message='Inserted successfully!')

    @endpoints.method(OpinionComment, RequestFeedback,
                        name='insert_new_comment',
                        path='app.insert_new_comment',
                        http_method='POST')
    def insert_new_comment(self, request):
        # Sanity check that opinion associated with comment exists.
        if not OpinionQuery.opinion_in_datastore(request.opinion_id):
            return RequestFeedback(status=AppErrors.OPINION_DOES_NOT_EXIST,
                error_message=('Opinion post with ID %s does not exist.')
                                % (request.opinion_id))

        OpinionCommentModel(Author=request.author, Text=request.text,
            Likes=request.likes, Dislikes=request.dislikes,
            CommentTimestampSec=request.timestamp_sec,
            OpinionID=request.opinion_id, CommentID=request.comment_id,
            id=request.comment_id).put()

        return RequestFeedback(status=AppErrors.NO_ERRORS,
                    error_message='Inserted successfully!')

    @endpoints.method(CommentWorkRequest, RequestFeedback,
                        name='delete_comment',
                        path='app.delete_comment',
                        http_method='POST')
    def delete_comment(self, request):
        if request.comment_id is None:
            return RequestFeedback(status=AppErrors.MISSING_INFORMATION,
                        error_message='Need comment id for this operation!')

        OpinionQuery.delete_comment_by_id(request.comment_id)
        return RequestFeedback(status=AppErrors.NO_ERRORS,
                    error_message='Deleted successfully!')

    @endpoints.method(OpinionWorkRequest, RequestFeedback,
                        name='delete_opinion',
                        path='app.delete_opinion',
                        http_method='POST')
    def delete_opinion(self, request):
        if request.opinion_id is None:
            return RequestFeedback(status=AppErrors.MISSING_INFORMATION,
                        error_message='Need opinion id for this operation!')

        # Get all comments with that opinion id.
        comments = OpinionQuery.get_comments_with_opinion_id(request.opinion_id)

        # Delete all those comments.
        for comment in comments:
            OpinionQuery.delete_comment_by_id(comment.CommentID)

        # Then delete the opinion.
        OpinionQuery.delete_opinion_by_id(request.opinion_id)

        return RequestFeedback(status=AppErrors.NO_ERRORS,
                    error_message='Deleted successfully!')

    @endpoints.method(OpinionWorkRequest, OpinionBundle,
                        name='retrieve_opinion',
                        path='app.retrieve_opinion',
                        http_method='GET')
    def retrieve_opinion(self, request):
        if request.opinion_id is None:
            return RequestFeedback(status=AppErrors.MISSING_INFORMATION,
                        error_message='Need opinion id for this operation!')

        # Grab necessary entities.
        opinion = OpinionQuery.get_opinion_by_id(request.opinion_id)
        comments = OpinionQuery.get_comments_with_opinion_id(request.opinion_id)

        c_list = BackendHelper.opinion_model_results_to_proto_list(comments)

        # Convert opinion entity to opinion proto.
        opinion_proto = BackendHelper.opinion_model_to_proto(opinion)
        return OpinionBundle(opinion=opinion_proto, comments=comments_list)

    @endpoints.method(OpinionListRequest, OpinionList,
                        name='retrieve_opinion_list',
                        path='app.retrieve_opinion_list',
                        http_method='GET')
    def retrieve_opinion_list(self, request):
        return OpinionList(opinion_list=OpinionQuery.get_opinion_list(request))

    @endpoints.method(CommentListRequest, CommentList,
                        name='retrieve_comment_list',
                        path='app.retrieve_comment_list',
                        http_method='GET')
    def retrieve_comment_list(self, request):
        return CommentList(comment_list=OpinionQuery.get_comment_list(request))

application = endpoints.api_server([OpinionAPI])
