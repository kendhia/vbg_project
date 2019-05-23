import pandas as pd
import numpy as np

flights_df = pd.read_csv("flights_reduced.csv", index_col=0)


# Adding  the new column reason, that will be the main attribute in our model 
flights_df["Reason"] = None


#removing the columns we won't use here
flights_df = flights_df.drop(labels=["DAY", "AIRLINE", "FLIGHT_NUMBER", "ORIGIN_AIRPORT", "DESTINATION_AIRPORT", "DAY_OF_WEEK", "FLIGHT_NUMBER", "TAIL_NUMBER", "DESTINATION_AIRPORT", "SCHEDULED_DEPARTURE"], axis=1)

# We have three different Classes of reasons.
reasons = ["Airline", "Security", "Weather", "unknown"]


#The logic behind labeling the data "aka reason"
taxt_out_mean = flights_df["TAXI_OUT"].mean()
taxt_in_mean = flights_df["TAXI_IN"].mean()
dep_time_mean = flights_df["DEPARTURE_TIME"].mean()

air_sys_delay_mean = flights_df["AIR_SYSTEM_DELAY"].mean()
sec_delay_mean = flights_df["SECURITY_DELAY"].mean()
late_aircraft_delay = flights_df["LATE_AIRCRAFT_DELAY"].mean()

weather_delay_mean = flights_df["WEATHER_DELAY"].mean()

for  index, row in  flights_df.iterrows():
    if ((row["TAXI_OUT"] > taxt_out_mean or row["TAXI_IN"] > taxt_in_mean)  and row["DEPARTURE_TIME"] > dep_time_mean):
        row["Reason"] = 0

    if (row["AIR_SYSTEM_DELAY"] > air_sys_delay_mean or row["SECURITY_DELAY"] > sec_delay_mean or row["LATE_AIRCRAFT_DELAY"] > late_aircraft_delay):
        row["Reason"] = 1

    if (row["WEATHER_DELAY"] > weather_delay_mean ):
        row["Reason"] = 2
    
    if row["Reason"] == None:
        row["Reason"] = 3

    flights_df.iloc[index] = row

flights_df.to_csv("flights_reason_added.csv")
