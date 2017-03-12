import json
import urllib
import urllib2

from google.appengine.api import urlfetch

from backend.proto import Post

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
    def handle_insert_new_post(post):
        url = ('http://localhost:8080'
                '/_ah/api/posts/v1/app.insert_new_post?');
        return RequestHandler.send_post_request(url, post)

    @staticmethod
    def handle_insert_new_comment(comment):
        url = ('http://localhost:8080'
                '/_ah/api/posts/v1/app.insert_new_comment?');
        return RequestHandler.send_post_request(url, comment)

    @staticmethod
    def handle_retrieve_post():
        url = ('http://localhost:8080'
                '/_ah/api/posts/v1/app.insert_new_comment?');

    @staticmethod
    def handle_retrieve_post_list(post_list_request):
        url = ('http://localhost:8080'
                '/_ah/api/posts/v1/app.retrieve_post_list?');
        return RequestHandler.send_get_request(url, post_list_request)

    @staticmethod
    def handle_retrieve_comment_list(comment_list_request):
        url = ('http://localhost:8080'
                '/_ah/api/posts/v1/app.retrieve_comment_list?');
        return RequestHandler.send_get_request(url, comment_list_request)

    @staticmethod
    def handle_delete_post():
        url = ('http://localhost:8080'
                '/_ah/api/posts/v1/app.delete_post?');

    @staticmethod
    def handle_delete_comment():
        url = ('http://localhost:8080'
                '/_ah/api/posts/v1/app.delete_comment?');
