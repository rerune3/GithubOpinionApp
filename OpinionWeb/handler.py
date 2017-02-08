import json
import urllib
import urllib2

from google.appengine.api import urlfetch

from backend.opinion_proto import Opinion

class RequestHandler(object):

    @staticmethod
    def send_post_request(url, data):
        data = urllib.urlencode(data)
        result = urlfetch.fetch(url=url + data, method=urlfetch.POST)
        return result.content

    @staticmethod
    def send_get_request(url, data):
        data = urllib.urlencode(data)
        result = urlfetch.fetch(url=url + data, method=urlfetch.GET)
        return result.content

    @staticmethod
    def handle_insert_new_opinion(opinion):
        url = ('http://localhost:8080'
                '/_ah/api/opinions/v1/app.insert_new_opinion?');
        return RequestHandler.send_post_request(url, opinion)

    @staticmethod
    def handle_insert_new_comment():
        url = ('http://localhost:8080'
                '/_ah/api/opinions/v1/app.insert_new_comment?');
        # return send_post_request_to_url(url, opinion)

    @staticmethod
    def handle_retrieve_opinion():
        url = ('http://localhost:8080'
                '/_ah/api/opinions/v1/app.insert_new_comment?');

    @staticmethod
    def handle_retrieve_opinion_list(opinion_list_request):
        url = ('http://localhost:8080'
                '/_ah/api/opinions/v1/app.retrieve_opinion_list?');
        return RequestHandler.send_get_request(url, opinion_list_request)

    @staticmethod
    def handle_delete_opinion():
        url = ('http://localhost:8080'
                '/_ah/api/opinions/v1/app.delete_opinion?');

    @staticmethod
    def handle_delete_comment():
        url = ('http://localhost:8080'
                '/_ah/api/opinions/v1/app.delete_comment?');
