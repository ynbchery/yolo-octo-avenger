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
		
class OnSubmit(base.Handler):
	def get(self):
		template_values = {
			'name': self.name,
			'verb': self.verb,
			'title': self.page_title,
			'desc': self.page_description
		}
		
		template = self.jinja_environment.get_template('index.html')
		self.response.out.write(template.render(template_values))
		
	def post(self):
		''' SETTING UP AN ENTITY GROUP & CREATE OBJECTS'''
		'''entitygroup = self.request.get("EntityGroup")'''
		entity = DataModel(	parent=EntityKey(entity_name),
							ndbname=self.request.get("ndbname"),
							ndbmessage=self.request.get("ndbmessage"))
							
		entity.put()
		self.redirect('/')
		
	