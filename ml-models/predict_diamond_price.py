import pandas as pd 
import dotenv
import os

dotenv.load_dotenv()

data_dir = os.getenv('DATA_DIR')

df = pd.read_csv(f'{data_dir}/diamonds.csv', index_col=0)

print(df.head())
