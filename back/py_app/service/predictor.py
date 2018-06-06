import pandas as pd
import glob
import sys
from datetime import datetime

data_file_pattern = '/*'

def read_data(files_path):
    files = glob.glob(files_path + data_file_pattern)

    list_of_dataframes = [pd.read_table(filename,  sep='|', encoding = "ISO-8859-1") for filename in files]
    list_of_processed_dataframes = []

    for data_frame in list_of_dataframes:
        list_of_processed_dataframes.append(clean_data(data_frame))

    combined_dataframes = pd.concat(list_of_processed_dataframes, ignore_index=True)
   
    return group_by_day_hour(combined_dataframes)


def clean_data(dataframe):
    dataframe = dataframe.drop(axis=1, index=0)
    return dataframe

def group_by_day_hour(dataframe):
    dataframe = dataframe.rename(columns={' FECHA_HORA_INICIO_LLAMADA ': 'end_call', ' FECHA_HORA_FIN_LLAMADA ': 'start_call'})
    dataframe = dataframe[["start_call"]]
    dataframe['criteria'] = dataframe.start_call.apply(lambda x: datetime.strptime(x.strip(), "%Y-%m-%d %H:%M:%S").replace(microsecond=0,second=0,minute=0))
    dataframe['criteria'] = dataframe.criteria.apply(lambda x: x.strftime('%Y-%m-%d %H'))
    dataframe = dataframe.groupby(['criteria']).size().reset_index(name='count')
    
    return dataframe


