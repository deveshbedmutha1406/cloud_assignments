import webapp2
import os
import json
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
	
	def get(self):
		a = 1
		b = 1
		for i in range(10):
			if i<2:
				self.response.write("{}<br>".format(a))
			else:
				var = a + b
				self.response.write("{}<br>".format(var))
				a = b
				b = var

		
		

app = webapp2.WSGIApplication(
	[("/", MainPage)],
	debug=True
)
