from google.appengine.ext import ndb

class CommentModel(ndb.Model):
    PostID = ndb.StringProperty(required=True)
    CommentID = ndb.StringProperty(required=True)
    Author = ndb.StringProperty(required=True)
    Text = ndb.StringProperty(required=False)
    Likes = ndb.IntegerProperty(required=False)
    Dislikes = ndb.IntegerProperty(required=False)
    CommentTimestampSec = ndb.IntegerProperty(required=True)

class PostModel(ndb.Model):
    Author = ndb.StringProperty(required=True)
    Tags = ndb.StringProperty(repeated=True)
    Text = ndb.StringProperty(required=True)
    Likes = ndb.IntegerProperty(required=False)
    Dislikes = ndb.IntegerProperty(required=False)
    PostTimestampSec = ndb.IntegerProperty(required=True)
    PostID = ndb.StringProperty(required=True)

class StructuredPostModel(ndb.Model):
    PostID = ndb.StringProperty(required=True)
    PostTimestampSec = ndb.IntegerProperty(required=True)

class TagsModel(ndb.Model):
    TagID = ndb.StringProperty(required=True)
    PostIDList = ndb.StructuredProperty(StructuredPostModel, repeated=True)
    # The last time the tag was created in a post or searched
    HitTimestampSec = ndb.IntegerProperty(required=True)
