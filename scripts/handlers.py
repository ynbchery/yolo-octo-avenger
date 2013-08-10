import webapp2
import logging
import os

from scripts import base

class MainHandler(base.Handler):
  def get(self):
    self.response.out.write("Hello")

class HomeHandler(base.Handler):
    def get(self):
		
        template_values = {
            'name': self.name,
            'verb': self.verb,
			'title': self.page_title,
            'desc': self.page_description
        }
		
        template = self.jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class FormHandler(base.Handler):
  def post(self):
    self.response.write('<html><body>You wrote:<pre>')
    self.response.write(cgi.escape(self.request.get('content')))
    self.response.write('</pre></body></html>')