from flask import Flask, jsonify, request
from datetime import datetime
import os
import socket
import service.predictor as model
import utils.utils as utils
import pandas as pd



app = Flask(__name__)



@app.route('/train-model')
def train():

    model.read_data('/data')
   
    return ('', 204)

@app.route('/CallCenterLoadForecast/v1/<string:timestamp>')
def predict(timestamp):

    country = request.args.get('country')
    personType = request.args.get('personType')
    globalSegment = request.args.get('globalSegment')
   
    return ""


@app.route('/_health')
def healthCheck():
    return utils.toJson({ "up" : "ok" })

if __name__ == "__main__":
    app.run(host="0.0.0.0")
