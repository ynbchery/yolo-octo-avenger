import webapp2
import logging
import os
import jinja2

from scripts import auth
from scripts import data

class Handler(webapp2.RequestHandler):
	''' SETTING UP JINJA2 '''
	jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
	
	page_title = "SystemsUnified"
	page_description = "A Cloud/IT company"
	name = "Jonathan"
	verb = "Love"
	
	''' AUTHENTICATION '''
	user = auth.Authenticate()
	
	''' DATABASES '''