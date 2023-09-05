import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from flask import Flask , request , render_template , jsonify
from key import creds
cred = credentials.Certificate(creds)

firebase_admin.initialize_app(cred)
db_client = firestore.client()
app = Flask(__name__)
@app.route('/' , methods = ['GET'])
def index():
    try:
        pot = db_client.collection('collection').document('document').get().to_dict()
        val = pot['field']
        return render_template('index.html' , value = val)

    except Exception as e:
        print(e)                      
        return jsonify({'status' : 'failed'})


if __name__  ==  "__main__":
    app.run(host = '0.0.0.0' , debug = True)
