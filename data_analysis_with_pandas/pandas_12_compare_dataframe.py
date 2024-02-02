import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

data = {'meters': [10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}

df = pd.DataFrame(data)

df['std'] = df['meters'].rolling(window=2).std() 

print(df)
#another aproach to set threshold 
df_std = df.describe()['meters']['std'] 

print(f" Threshold standard deviation : {df_std}")

df = df[(df['std'] < df_std )]


df['meters'].plot()
print(df['meters'])
plt.show()
