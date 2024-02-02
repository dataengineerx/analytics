import pandas as pd 

index = pd.date_range('1/1/2000', periods=100, freq='min')
series = pd.Series(range(100), index=index)
print(series)

# Downsample the series into 3 minute bins and sum the values of the timestamps falling into a bin.

series_3min = series.resample('D').sum()

print(series_3min)

