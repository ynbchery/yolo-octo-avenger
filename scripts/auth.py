from google.appengine.api import users

import webapp2

class Authenticate(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    
    if not user:
      self.redirect(users.CreateLoginURL(self.request.uri))
    else:
      return user