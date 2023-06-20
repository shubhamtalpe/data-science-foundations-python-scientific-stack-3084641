# What is the mean speed (mile/hour) in taxi.parquet?

# - Run download_data.py to download the data

# %%

import pandas as pd
import numpy as np

# %%
df = pd.read_parquet("taxi.parquet")
df.head()
# %%
df = df[df["tpep_dropoff_datetime"] > df["tpep_pickup_datetime"]]
df.head()
# %%
times = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
times = times / pd.Timedelta(1, "hour")
times[:5]
# %%
speed = df["trip_distance"] / times
speed[:5]
# %%
np.dtype(speed)
# %%
speed.mean()
# %%
