from flask import Flask
from flask import request
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return -1



@app.route('/sentiment/', methods = ['GET', 'POST', 'PUT'])
def get_sentiments():
	print('something')
	if request.method == 'POST':
		####call olga's code
		return json.dumps({'sentiment_score': -1})
		return score







@app.route('/face/', methods = ['GET'])
def get_face():
    if request.method == 'GET':
    	####call ravit's
    	return score


if __name__ == '__main__':
    app.run()
