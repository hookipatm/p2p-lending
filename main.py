#!/usr/bin/env python
#

import webapp2
import wsgiref.handlers
from google.appengine.ext import webapp
from views import *

def main():
  wsgiref.handlers.CGIHandler().run(app)
  
app = webapp.WSGIApplication([
  ('/', IndexHandler),
  ('/notes', NotesHandler)
], debug=True)
