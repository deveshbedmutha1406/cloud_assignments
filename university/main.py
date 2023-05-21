import os
import urllib
import webapp2
import json
from google.appengine.ext.webapp import template

class HomePage(webapp2.RedirectHandler):
    ROOT = os.path.dirname(__file__)

    def get(self):
        path = os.path.join(self.ROOT, "templates/home.html")
        self.response.out.write(template.render(path, {}))

    def post(self):
        name = self.request.get('name')
        url = "http://universities.hipolabs.com/search?name={0}".format(name)
        data = urllib.urlopen(url).read()
        obj = json.loads(data)
        path = os.path.join(self.ROOT, "templates/home.html")
        self.response.out.write(template.render(path, {"data": obj}))
        


    

app = webapp2.WSGIApplication(
    [("/", HomePage)],
    debug=True
)