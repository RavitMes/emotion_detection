from flask import Flask
from flask import request
import json
from flask_cors import CORS
from text_sentiment import *
from face_detector import FaceDetector
from keras.models import load_model

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return -1



@app.route('/sentiment/', methods = ['GET', 'POST', 'PUT'])
def get_sentiments():
	if request.method == 'POST':
		#get page sentiment
		ts = TextSentiment()
		sentiment = ts.get_sentiment(request.data)
		#get the face emotion score
		face_detector = FaceDetector()
		face_score = face_detector.get_face_and_predict()

		if face_score > 0.3:
			print(f"FACE SCORE IS SAD. SCORE: {face_score}")
			if sentiment < 0:
				print(f"PAGE SCORE IS SAD TOO! SCORE: {sentiment}")
				return json.dumps({'sentiment_score': -1})
			else:
				print(f"PAGE SCORE IS NOT SAD. SCORE: {sentiment}")
				return json.dumps({'sentiment_score': 1})
		else:
			print(f"FACE SCORE WAS NOT SAD. SCORE: {sentiment}")
			return json.dumps({'sentiment_score': 1})







@app.route('/face/', methods = ['GET'])
def get_face():
    if request.method == 'GET':
    	####call ravit's
    	return score


if __name__ == '__main__':
    app.run()
