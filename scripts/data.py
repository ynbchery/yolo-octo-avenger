import cgi
import urllib
import webapp2
import os
import logging

from google.appengine.ext import ndb

DEFAULT_ENTITY_NAME = "DefaultEntityGroup"

def EntityKey(entity_name=DEFAULT_ENTITY_NAME):
	''' CREATES A DATASTORE KEY '''
	return ndb.Key("OnSubmit", entity_name)

class DataModel(ndb.Model):
	''' SETTING UP A MODEL FOR STORING DATA '''
	ndbname = ndb.StringProperty()
	ndbmessage = ndb.TextProperty(indexed=False)
	ndbdate = ndb.DateTimeProperty(auto_now_add=True)
	
