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

    model.trainning('/data')

    return ('', 204)

@app.route('/CallCenterLoadForecast/v1/<string:timestamp>')
def predict(timestamp):
    country = request.args.get('country')
    personType = request.args.get('personType')
    globalSegment = request.args.get('globalSegment')

    if (country or personType or globalSegment):
        list_params = []
        if (country):
            list_params.append('country')
        elif (personType):
            list_params.append('personType')
        elif (globalSegment):
            list_params.append('globalSegment')

        filters = utils.convertParamToColumn(list_params)

        model.dynamic_trainning('/data',filters,country,personType,globalSegment)

        return ('', 204)

    return jsonify(model.predict_phoncalls_date(timestamp))


@app.route('/_health')
def healthCheck():
    return utils.toJson({ "up" : "ok" })

if __name__ == "__main__":
    app.run(host="0.0.0.0")
