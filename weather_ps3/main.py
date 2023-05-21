import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    ROOT = os.path.dirname(__file__)

    def get(self):
        path = os.path.join(self.ROOT, "templates/home.html")
        self.response.out.write(template.render(path, {}))
    
    def post(self):
        lat = self.request.get("lat")
        long = self.request.get("long")
        ans = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&hourly=temperature_2m&forecast_days=2".format(lat, long)
        data = urllib.urlopen(ans).read()
        self.response.out.write(data)

app = webapp2.WSGIApplication(
    [('/', MainPage)],
    debug=True
)