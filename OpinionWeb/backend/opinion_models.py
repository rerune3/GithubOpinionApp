from google.appengine.ext import ndb

class OpinionCommentModel(ndb.Model):
    OpinionID = ndb.StringProperty(required=True)
    CommentID = ndb.StringProperty(required=True)
    Author = ndb.StringProperty(required=True)
    Text = ndb.StringProperty(required=False)
    Likes = ndb.IntegerProperty(required=False)
    Dislikes = ndb.IntegerProperty(required=False)
    CommentTimestampSec = ndb.IntegerProperty(required=True)

class OpinionModel(ndb.Model):
    Author = ndb.StringProperty(required=True)
    Tags = ndb.StringProperty(repeated=True)
    Text = ndb.StringProperty(required=True)
    Likes = ndb.IntegerProperty(required=False)
    Dislikes = ndb.IntegerProperty(required=False)
    OpinionTimestampSec = ndb.IntegerProperty(required=True)
    OpinionID = ndb.StringProperty(required=True)
