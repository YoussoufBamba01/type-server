#!/usr/bin/python

import firebase_admin
import time
from firebase_admin import credentials, firestore



cred = credentials.Certificate("C:/Users/HP/Projects/Article/Posts/cpanel5427-firebase-adminsdk-cqc0e-710b2a8e0c.json")


firebase = firebase_admin.initialize_app(cred)
db = firestore.client()


def recordata(value):
	if (value != 0):
	  sensor_ref= db.collection(u'mesures')
	  moisture_ref= sensor_ref.document(u'moisture')
	  moisture_ref.add({u'value': value})
	  print(value)
	  
