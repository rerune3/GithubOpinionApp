from google.appengine.ext import ndb

from app_errors import AppErrors

from backend_helper import BackendHelper

from opinion_models import OpinionModel
from opinion_models import OpinionCommentModel

from opinion_proto import OpinionListRequest

class OpinionQuery(object):

    @staticmethod
    def opinion_in_datastore(opinion_id):
        return not (OpinionQuery.get_opinion_by_id(opinion_id) is None)

    @staticmethod
    def delete_opinion_by_id(opinion_id):
        ndb.Key('OpinionModel', opinion_id).delete()

    @staticmethod
    def delete_comment_by_id(comment_id):
        ndb.Key('OpinionCommentModel', comment_id).delete()

    @staticmethod
    def get_opinion_by_id(opinion_id):
        return ndb.Key('OpinionModel', opinion_id).get()

    @staticmethod
    def get_comment_list(list_request):
        results = ndb.gql(('SELECT * FROM OpinionCommentModel '
                          'WHERE OpinionID = :1'), list_request.opinion_id)
        return BackendHelper.comment_model_results_to_proto_list(results)

    @staticmethod
    def get_opinion_list(list_request):
        results = ndb.gql('SELECT * FROM OpinionModel ORDER BY '
                          'OpinionTimestampSec DESC LIMIT 50')
        return BackendHelper.opinion_model_results_to_proto_list(results)
