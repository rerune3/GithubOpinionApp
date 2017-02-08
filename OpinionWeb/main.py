import os
import json
import jinja2
import webapp2

from handler import RequestHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

APPLICATION_USER = {}

class LoginPage(webapp2.RequestHandler):
    user_info = {}

    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('login.html')
        self.response.write(template.render(template_values))

    def post(self):
        user_info = json.loads(self.request.body)
        print(APPLICATION_USER)

class HomePage(webapp2.RequestHandler):

    def get(self):
        print(self.request.body)

        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.write(template.render(template_values))

    def post(self):
        request = json.loads(self.request.get('request_type'))
        if request == 'INSERT_NEW_OPINION':
            opinion = json.loads(self.request.get('opinion'))
            response = RequestHandler.handle_insert_new_opinion(opinion)
            self.response.write(response)
        elif request == 'INSERT_NEW_COMMENT':
            response = RequestHandler.handle_insert_new_comment()
            self.response.write(response)
        elif request == 'RETRIEVE_OPINION':
            response = RequestHandler.handle_insert_new_comment()
            self.response.write(response)
        elif request == 'RETRIEVE_OPINION_LIST':
            request_json = self.request.get('opinion_list_request')
            opinion_list_request = json.loads(request_json)
            response = RequestHandler.handle_retrieve_opinion_list(
                                                        opinion_list_request)
            self.response.write(response)
        elif request == 'DELETE_OPINION':
            response = RequestHandler.handle_insert_new_comment()
            self.response.write(response)
        elif request == 'DELETE_COMMENT':
            response = RequestHandler.handle_insert_new_comment()
            self.response.write(response)
        else:
            print('Unknown request type %s', request)
            return

        template_values = {}
        # template = JINJA_ENVIRONMENT.get_template('home.html')
        # self.response.write(template.render(template_values)


application = webapp2.WSGIApplication([
    ('/', LoginPage), ('/home', HomePage)], debug=True)
