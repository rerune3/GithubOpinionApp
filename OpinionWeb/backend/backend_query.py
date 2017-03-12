from google.appengine.ext import ndb

from app_errors import AppErrors

from backend_helper import BackendHelper

from models import PostModel
from models import CommentModel

from proto import PostListRequest

class PostQuery(object):

    @staticmethod
    def post_in_datastore(post_id):
        return not (PostQuery.get_post_by_id(post_id) is None)

    @staticmethod
    def delete_post_by_id(post_id):
        ndb.Key('PostModel', post_id).delete()

    @staticmethod
    def delete_comment_by_id(comment_id):
        ndb.Key('CommentModel', comment_id).delete()

    @staticmethod
    def get_post_by_id(post_id):
        return ndb.Key('PostModel', post_id).get()

    @staticmethod
    def get_comment_list(list_request):
        results = ndb.gql(('SELECT * FROM CommentModel '
                          'WHERE PostID = :1'), list_request.post_id)
        return BackendHelper.comment_model_results_to_proto_list(results)

    @staticmethod
    def get_post_list(list_request):
        results = ndb.gql('SELECT * FROM PostModel ORDER BY '
                          'PostTimestampSec DESC LIMIT 50')
        return BackendHelper.post_model_results_to_proto_list(results)
