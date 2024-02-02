import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

fig = plt.figure()
ax1 = plt.subplot2grid((2,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0),sharex=ax1)

hpi_df = pd.read_pickle('/home/cyborg15/projects/analytics/data_analysis_with_pandas/data/fmac_all_states.pickle')

def tx_moving_average_and_stddev(hpi_df):
    hpi_df['TX12MA'] =  hpi_df['TX'].rolling(window=12).mean()
    hpi_df['TX12STD'] =  hpi_df['TX'].rolling(window=12).std()
    print(hpi_df[['TX','TX12MA','TX12STD']])
    hpi_df[['TX','TX12MA']].plot(ax = ax1 )
    hpi_df[['TX12STD']].plot(ax = ax2 )



def correlation_between_states(hpi_df):
    hpi_df['TX'].plot(ax = ax1, label='Monthly TX HPI')
    hpi_df['AK'].plot(ax = ax1, label='Monthly AK HPI')
    ax1.legend(loc=4)

    hpi_df_corr_tx_ak = hpi_df['TX'].rolling(window=12).corr(hpi_df['AK'])
    hpi_df_corr_tx_ak.plot(ax = ax2, label='TX_AK_HPI_Corr')
            



plt.show()