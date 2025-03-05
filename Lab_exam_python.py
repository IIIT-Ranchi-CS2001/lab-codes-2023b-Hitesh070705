import numpy as np
import pandas as pd

df=pd.read_csv("AQI_Data.csv")
df.head()

# (a)
print("First 8 rows of the dataset:")
df.head(8)

# (b)
print("Last 5 rows of the dataset:")
df.tail(5)

# (c)
df.info()

# (d)
mean_aqi_per_city = {city: np.mean(df['AQI'][df['City'] == city]) for city in np.unique(df['City'])}
max_PM_per_city= {city: np.max(df['PM2.5'][df['City'] == city]) for city in np.unique(df['City'])}
min_PM10_per_city={city: np.min(df['PM10'][df['City'] == city]) for city in np.unique(df['City'])}
print("Mean AQI per city: ",mean_aqi_per_city)
print("Max PM per city: ",max_PM_per_city)
print("Min PM10 per city: ",min_PM10_per_city)

# (3)
stats = df.groupby("City").agg(
    mean_AQI=("AQI", "mean"),
    max_PM2_5=("PM2.5", "max"),
    min_PM10=("PM10", "min")
)


city_stats_dict = stats.to_dict()


print(city_stats_dict)