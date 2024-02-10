import pandas as pd
import os
import quandl
import matplotlib.pyplot as plt
import pickle
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
    # df = df.resample('D').mean()
    df = df.resample("M").mean()
    return df


m30_df = mortgage_30y()
m30_df.columns = ["M30"]

hpi_df = pd.read_pickle(DATA_DIR + "fmac_all_states.pickle").drop(
    ["United States not seasonaly adjusted", "United States seasonaly adjusted"], axis=1
)

joined_df = hpi_df.join(m30_df)

#filter m30 = 1 


print(joined_df.corr()["M30"])

print(joined_df.corr()["M30"].describe())
