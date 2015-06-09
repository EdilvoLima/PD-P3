__author__ = 'Edilvo'

from google.appengine.ext import db

class Weather(db.Model):
    temp1 = db.IntegerProperty(required=True)
    temp2 = db.IntegerProperty(required=True)
    temp3 = db.IntegerProperty(required=True)
    humidity1 = db.IntegerProperty(required=True)
    humidity2 = db.IntegerProperty(required=True)
    humidity3 = db.IntegerProperty(required=True)
    data = db.DateTimeProperty(auto_now_add=True)