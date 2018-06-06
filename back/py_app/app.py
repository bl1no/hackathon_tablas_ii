from flask import Flask, jsonify, request
from datetime import datetime
import os
import socket
import service.predictor as model
import utils.utils as utils
import pandas as pd



app = Flask(__name__)



@app.route('/data/<string:year>/<string:month>/<string:day>/<string:hour>')
def getData(year,month,day,hour):

    filters = request.args.get('filters')

    data = model.read_data('/data')
   
    return data.to_json()


@app.route('/_health')
def healthCheck():
    return utils.toJson({ "up" : "ok" })

if __name__ == "__main__":
    app.run(host="0.0.0.0")
