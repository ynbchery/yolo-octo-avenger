import webapp2
import logging
import os
import jinja2

from scripts import auth

class Handler(webapp2.RequestHandler):
  def get(self):
    user = auth.Authenticate()
    page_title = "SystemsUnified"
    page_description = "A Cloud/IT company"
  
  @webapp2.cached_property
  def User(self):
    return user
  
  ''' SETTING UP JINJA2 '''
  jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'templates')))
