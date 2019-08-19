#!/usr/bin/python

import firebase_admin
import time
from firebase_admin import credentials, firestore


cred = credentials.Certificate("path/to/file.json")
delay = 1

firebase = firebase_admin.initialize_app(cred)
db = firestore.client()

 
def recordata():
  sensor_ref= db.collection(u'mesures')
  moisture_ref= sensor_ref.document(u'moisture')
  moisture_ref.set(form.body)
  print(form.body)
  if (form.title != 0):
  time.sleep(delay)
