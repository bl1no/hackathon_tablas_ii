from flask import Flask
import os
import socket
import pandas as pd

app = Flask(__name__)


@app.route('/data')
def getData():
    
    data_201706 = pd.read_table('/data/201706_linea_ident.txt',  sep='|', encoding = "ISO-8859-1")
    data_201706 = data_201706.drop(axis=1, index=0)
    result = { "data" : data_201706.head()}
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
