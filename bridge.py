import serial
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from flask import Flask , request , render_template , jsonify
from key import creds
import time
cred = credentials.Certificate(creds)

firebase_admin.initialize_app(cred)
db_client = firestore.client()

ser = serial.Serial('COM3')
if not ser.isOpen():
    ser.open()
print('com3 is open', ser.isOpen())


while True:
    pot_val = ser.readline().strip()
    values = pot_val.decode('ascii')
    db_client.collection('collection').document('document').set({'field' : values})
    print(values)
    time.sleep(0.5)
    
    
