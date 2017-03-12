from google.appengine.ext import endpoints
from google.appengine.ext import ndb
from protorpc import message_types
from protorpc import remote

from app_errors import AppErrors

from backend_helper import BackendHelper
from backend_query import PostQuery

from models import PostModel
from models import CommentModel

from proto import CommentListResponse
from proto import CommentListRequest
from proto import CommentWorkRequest
from proto import PostWorkRequest
from proto import PostListRequest
from proto import PostBundle
from proto import Post
from proto import Comment
from proto import PostListResponse
from proto import RequestFeedback

import uuid

@endpoints.api(name='posts', version='v1', description='API for Posts')
class PostAPI(remote.Service):

    @endpoints.method(Post, RequestFeedback,
                        name='insert_new_post',
                        path='app.insert_new_post',
                        http_method='POST')
    def insert_new_post(self, request):
        unique_post_id = uuid.uuid4().hex
        if PostQuery.post_in_datastore(unique_post_id):
            return RequestFeedback(status=AppErrors.ID_ALREADY_EXISTS,
                error_message=('Post post with ID %s already exists. awk..')
                                % (request.post_id))

        PostModel(Author=request.author, Tags=request.tags,
                    Text=request.text, Likes=request.likes,
                    Dislikes=request.dislikes,
                    PostTimestampSec=request.timestamp_sec,
                    PostID=unique_post_id,
                    id=unique_post_id).put()

        return RequestFeedback(status=AppErrors.NO_ERRORS,
                    error_message='Inserted successfully!',
                    unique_id=unique_post_id)

    @endpoints.method(Comment, RequestFeedback,
                        name='insert_new_comment',
                        path='app.insert_new_comment',
                        http_method='POST')
    def insert_new_comment(self, request):
        # Sanity check that post associated with comment exists.
        if not PostQuery.post_in_datastore(request.post_id):
            return RequestFeedback(status=AppErrors.POST_DOES_NOT_EXIST,
                error_message=('Post post with ID %s does not exist.')
                                % (request.post_id))

        unique_comment_id = uuid.uuid4().hex
        CommentModel(Author=request.author, Text=request.text,
            Likes=request.likes, Dislikes=request.dislikes,
            CommentTimestampSec=request.timestamp_sec,
            PostID=request.post_id, CommentID=unique_comment_id,
            id=unique_comment_id).put()

        return RequestFeedback(status=AppErrors.NO_ERRORS,
                    error_message='Inserted successfully!',
                    unique_id=unique_comment_id)

    @endpoints.method(CommentWorkRequest, RequestFeedback,
                        name='delete_comment',
                        path='app.delete_comment',
                        http_method='POST')
    def delete_comment(self, request):
        if request.comment_id is None:
            return RequestFeedback(status=AppErrors.MISSING_INFORMATION,
                        error_message='Need comment id for this operation!')

        PostQuery.delete_comment_by_id(request.comment_id)
        return RequestFeedback(status=AppErrors.NO_ERRORS,
                    error_message='Deleted successfully!')

    @endpoints.method(PostWorkRequest, RequestFeedback,
                        name='delete_post',
                        path='app.delete_post',
                        http_method='POST')
    def delete_post(self, request):
        if request.post_id is None:
            return RequestFeedback(status=AppErrors.MISSING_INFORMATION,
                        error_message='Need post id for this operation!')

        # Get all comments with that post id.
        comments = PostQuery.get_comments_with_post_id(request.post_id)

        # Delete all those comments.
        for comment in comments:
            PostQuery.delete_comment_by_id(comment.CommentID)

        # Then delete the post.
        PostQuery.delete_post_by_id(request.post_id)

        return RequestFeedback(status=AppErrors.NO_ERRORS,
                    error_message='Deleted successfully!')

    @endpoints.method(PostWorkRequest, PostBundle,
                        name='retrieve_post',
                        path='app.retrieve_post',
                        http_method='GET')
    def retrieve_post(self, request):
        if request.post_id is None:
            return RequestFeedback(status=AppErrors.MISSING_INFORMATION,
                        error_message='Need post id for this operation!')

        # Grab necessary entities.
        post = PostQuery.get_post_by_id(request.post_id)
        comments = PostQuery.get_comments_with_post_id(request.post_id)

        c_list = BackendHelper.post_model_results_to_proto_list(comments)

        # Convert post entity to post proto.
        proto = BackendHelper.post_model_to_proto(post)
        return PostBundle(post=proto, comments=comments_list)

    @endpoints.method(PostListRequest, PostListResponse,
                        name='retrieve_post_list',
                        path='app.retrieve_post_list',
                        http_method='GET')
    def retrieve_post_list(self, request):
        return PostListResponse(
                        post_list=PostQuery.get_post_list(request))

    @endpoints.method(CommentListRequest, CommentListResponse,
                        name='retrieve_comment_list',
                        path='app.retrieve_comment_list',
                        http_method='GET')
    def retrieve_comment_list(self, request):
        return CommentListResponse(
                        comment_list=PostQuery.get_comment_list(request))

application = endpoints.api_server([PostAPI])
