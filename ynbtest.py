import webapp2
import os

from webapp2_extras import routes
from scripts import handlers

IS_DEBUG_TRUE = os.environ.get("SERVER_SOFTWARE", "").startswith("Dev") # Verifies if running dev server(true) or production server(false)

webapp2_config = {}
webapp2_config["webapp2_extras.sessions"] = {
  "secret_key":"suSECRETkey",
}

app = webapp2.WSGIApplication([
  webapp2.Route(r'/main', handler=handlers.MainHandler, name="main"), \
  webapp2.Route(r'/', handler=handlers.HomeHandler, name="home"), \
  webapp2.Route(r'/sign', handler=handlers.FormHandler, name="forms"),
  
], debug=IS_DEBUG_TRUE)