import pandas as pd
import os
import quandl 
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import dotenv

dotenv.load_dotenv()
style.use('fivethirtyeight')

API_KEY = os.getenv("QUANDL_API_KEY")

def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=API_KEY)
    print(f"initial dataframe")
    print(df.head(5))
    df["Value1"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    # df = df.resample('D').mean()
    df = df.resample('M').mean()
    print("resampled dataframe")
    print(df.head(50))
    return df

df =  mortgage_30y()

df.p



