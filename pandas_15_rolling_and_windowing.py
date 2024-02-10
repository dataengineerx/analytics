import pandas as pd
import os
import quandl
from matplotlib import style
import dotenv

dotenv.load_dotenv()
style.use("fivethirtyeight")

API_KEY = os.getenv("QUANDL_API_KEY")
DATA_DIR = os.getenv("DATA_DIR")


def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=API_KEY)
    print(f"initial dataframe")
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample('D').mean()
    df = df.resample("M").mean()
    df.columns = ["M30"] 
    return df

def sp500_data():
    df = quandl.get("MULTPL/SP500_REAL_PRICE_MONTH", trim_start="1975-01-01", authtoken=API_KEY)
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
    df = df.resample("M").mean()
    return df   

def us_unemployment():
    df = quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=API_KEY) #todo fix this source
    df["Unemployment Rate"] = (df["Unemployment Rate"] - df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df = df.resample("1D").mean()
    df = df.resample("M").mean()
    return df

def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=API_KEY) #TODO fix this source
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample("M").mean()
    df.rename(columns={"Value": "GDP"}, inplace=True)
    df = df["GDP"]
    return df

def label_data(input_column):
    if input_column > 0:
        return 1
    else:
        return 0
    

hpi_data = pd.read_pickle(DATA_DIR + "states.pickle")
print(hpi_data)
hpi_bench_df = pd.read_pickle(DATA_DIR + "fmac_all_states.pickle").drop(
    ["United States not seasonaly adjusted", "United States seasonaly adjusted"], axis=1
)
m30_df = mortgage_30y()
m30_df["label"] = list(map(label_data, m30_df["M30"]))
print(m30_df)

import numpy as np

X = np.array(m30_df.drop(["label"],axis=1))
print(X)
 