import pandas as pd
import glob
import sys
import numpy as np
from datetime import datetime
from statsmodels.tsa.arima_model import ARIMA
from sklearn.linear_model import LinearRegression

data_file_pattern = '/*'
data_trained_model = '/trainning/output.model'

def trainning(files_path):
    files = glob.glob(files_path + data_file_pattern)

    list_of_dataframes = [pd.read_table(filename,  sep='|', encoding = "ISO-8859-1") for filename in files]
    list_of_processed_dataframes = []

    for data_frame in list_of_dataframes:
        list_of_processed_dataframes.append(clean_data(data_frame))

    combined_dataframes = pd.concat(list_of_processed_dataframes, ignore_index=True)
   
    procesed_dataframe = group_by_day_hour(combined_dataframes)

    procesed_dataframe.to_csv(data_trained_model, sep='\t', encoding='utf-8', index=False)

def dynamic_trainning(files_path, filters):
    files = glob.glob(files_path + data_file_pattern)

    list_of_dataframes = [pd.read_table(filename,  sep='|', encoding = "ISO-8859-1") for filename in files]
    list_of_processed_dataframes = []

    for data_frame in list_of_dataframes:
        list_of_processed_dataframes.append(clean_data(data_frame))

    combined_dataframes = pd.concat(list_of_processed_dataframes, ignore_index=True)
   
    procesed_dataframe = dynamic_group_by(combined_dataframes,filters)

    procesed_dataframe.to_csv(data_trained_model, sep='\t', encoding='utf-8', index=False)

def clean_data(dataframe):
    dataframe = dataframe.drop(axis=1, index=0)
    return dataframe

def group_by_day_hour(dataframe):
    dataframe = dataframe.rename(columns={' FECHA_HORA_INICIO_LLAMADA ': 'end_call', ' FECHA_HORA_FIN_LLAMADA ': 'start_call'})
    dataframe = dataframe[["start_call"]]
    dataframe['criteria'] = dataframe.start_call.apply(lambda x: datetime.strptime(x.strip(), "%Y-%m-%d %H:%M:%S").replace(microsecond=0,second=0,minute=0))
    dataframe['criteria'] = dataframe.criteria.apply(lambda x: x.strftime('%Y-%m-%d %H'))
    dataframe = dataframe.groupby(['criteria']).size().reset_index(name='count')
    return dataframe[['criteria','count']]

def dynamic_group_by(dataframe, filters):
    dataframe = dataframe.rename(columns={' FECHA_HORA_INICIO_LLAMADA ': 'end_call', ' FECHA_HORA_FIN_LLAMADA ': 'start_call'})
    dataframe = dataframe[["start_call"]]
    dataframe['criteria'] = dataframe.start_call.apply(lambda x: datetime.strptime(x.strip(), "%Y-%m-%d %H:%M:%S").replace(microsecond=0,second=0,minute=0))
    dataframe['criteria'] = dataframe.criteria.apply(lambda x: x.strftime('%Y-%m-%d %H'))
    dataframe = dataframe.groupby(['criteria']).size().reset_index(name='count')
    return dataframe[['criteria','count']]

def predict_phoncalls_date(timestamp):
    dataframe = pd.read_table(data_trained_model, sep='\t', encoding='utf-8')
    model = LinearRegression()
    dataframe['criteria'] = dataframe.criteria.apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H').timestamp())

    result = model.fit(dataframe[['criteria','count']], dataframe[['criteria','count']])

    return result.to_string()

