__author__ = 'Edilvo'

from google.appengine.ext import db

class Mail(db.Model):
    email = db.StringProperty(required=True)