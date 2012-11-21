#!/usr/bin/env python

import os
import datetime
import logging
import time

from google.appengine.api import urlfetch
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from models import *

header = os.path.join(os.path.dirname(__file__) + '/templates/', 'header.html')
footer = os.path.join(os.path.dirname(__file__) + '/templates/', 'footer.html')

class IndexHandler(webapp.RequestHandler):
  def get(self):
    template_values = {'data': 'toto' }
    path = os.path.join(os.path.dirname(__file__) + '/templates/', 'index.html')
    self.response.out.write(template.render(header, {}))
    self.response.out.write(template.render(path, template_values))
    self.response.out.write(template.render(footer, {}))
    
    
class NotesHandler(webapp.RequestHandler):
  def get(self):
    template_values = {'data': 'toto' }
    path = os.path.join(os.path.dirname(__file__) + '/templates/', 'notes.html')
    self.response.out.write(template.render(header, {}))
    self.response.out.write(template.render(path, template_values))
    self.response.out.write(template.render(footer, {}))