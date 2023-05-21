import os 
import webapp2
import urllib
import json
from google.appengine.ext.webapp import template

ROOT = os.path.dirname(__file__)

class HomePage(webapp2.RequestHandler):
	def get(self):
		path = os.path.join(ROOT, "templates/home.html")
		self.response.out.write(template.render(path, {}))
	
	def post(self):
		pin = self.request.get('zip_code')
		branch = self.request.get('branch')
		print(branch)
		if len(pin) != 0:
			ans = "https://api.postalpincode.in/pincode/{0}".format(pin)
		else:
			ans = "https://api.postalpincode.in/postoffice/{0}".format(branch)
		data = urllib.urlopen(ans).read()
		obj = json.loads(data)
		name = obj[0]['PostOffice'][0]['Name']
		district = obj[0]['PostOffice'][0]['District']
		region = obj[0]['PostOffice'][0]['Region']
		di = {"name": name, "district": district, "region": region}
		print(di)
		path = os.path.join(ROOT, "templates/info.html")
		self.response.out.write(template.render(path, di))
		
app = webapp2.WSGIApplication(
	[("/", HomePage)],
	debug=True
)
