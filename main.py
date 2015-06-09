__author__ = 'Edilvo'

from flask import Flask, request
from MailModel import Mail
from WeatherModel import Weather
from google.appengine.api import mail
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'App Engine - Programacao Distribuida - 2015'

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        e = Mail(
            email = request.form.get('email'),
        )
        email_query = Mail.all()
        for ema in email_query:
            if ema.email == e.email:
                return 'Email '+ema.email+' ja cadastrado!'
        e.put()
        em = request.form.get('email')
    if request.method == 'GET':
        e = Mail(
            email = request.args.get('email'),
        )
        email_query = Mail.all()
        for ema in email_query:
            if ema.email == e.email:
                return 'Email '+ema.email+' ja cadastrado!'
        e.put()
        em = request.args.get('email')
    return 'Email '+em+' cadastrado!'

@app.route('/storage', methods=['GET', 'POST'])
def storage():
    if request.method == 'POST':
        w = Weather(
            temp1 = int(request.form.get('temp1')),
            temp2 = int(request.form.get('temp2')),
            temp3 = int(request.form.get('temp3')),
            humidity1 = int(request.form.get('humidity1')),
            humidity2 = int(request.form.get('humidity2')),
            humidity3 = int(request.form.get('humidity3')),
        )
        w.put()
        if ((w.temp1 > 28 or w.temp1 < 40) and (w.humidity1 > 20 or w.humidity1 < 30)) or ((w.temp2 > 28 or w.temp2 < 40) and (w.humidity2 > 20 or w.humidity2 < 30)) or ((w.temp3 > 28 or w.temp3 < 40) and (w.humidity3 > 20 or w.humidity3 < 30)):
            email = 'Weather Alert!'
            email = email + '\nCity1: ' + '\nTemp: ' + request.form.get('temp1')
            email = email + '\nCity2: ' + '\nTemp: ' + request.form.get('temp2')
            email = email + '\nCity3: ' + '\nTemp: ' + request.form.get('temp3')
            email = email + '\nCity1: ' + '\nHumidity: ' + request.form.get('humidity1')
            email = email + '\nCity2: ' + '\nHumidity: ' + request.form.get('humidity2')
            email = email + '\nCity3: ' + '\nHumidity: ' + request.form.get('humidity3')
            email_query = Mail.all()
            for e in email_query:
                mail.send_mail("Weather@pd-p3-00.appspotmail.com",
                           e.email,
                          "Drink plenty of water!",
                            email)

    if request.method == 'GET':
        w = Weather(
            temp1 = int(request.args.get('temp')),
            temp2 = int(request.args.get('temp')),
            temp3 = int(request.args.get('temp')),
            humidity1 = int(request.args.get('humidity')),
            humidity2 = int(request.args.get('humidity')),
            humidity3 = int(request.args.get('humidity')),
        )
        w.put()
        if ((w.temp1 > 28 or w.temp1 < 40) and (w.humidity1 > 20 or w.humidity1 < 30)) or ((w.temp2 > 28 or w.temp2 < 40) and (w.humidity2 > 20 or w.humidity2 < 30)) or ((w.temp3 > 28 or w.temp3 < 40) and (w.humidity3 > 20 or w.humidity3 < 30)):
            email = 'Weather Alert!'
            email = email + '\nCity1: ' + '\nTemp: ' + request.args.get('temp1')
            email = email + '\nCity2: ' + '\nTemp: ' + request.args.get('temp2')
            email = email + '\nCity3: ' + '\nTemp: ' + request.args.get('temp3')
            email = email + '\nCity1: ' + '\nHumidity: ' + request.args.get('humidity1')
            email = email + '\nCity2: ' + '\nHumidity: ' + request.args.get('humidity2')
            email = email + '\nCity3: ' + '\nHumidity: ' + request.args.get('humidity3')
            email_query = Mail.all()
            for e in email_query:
                mail.send_mail("Weather@pd-p3-00.appspotmail.com",
                           e.email,
                          "Drink plenty of water!",
                            email)

    return 'salvo com sucesso'

