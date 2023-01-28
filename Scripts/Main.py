import yfinance as yf
import pandas as pd
import time
import pytz
from datetime import datetime


def create_data(interval, currency="EURUSD=X", period="5d"):
    file_name = "CachedData/"+currency+"_"+interval
    tz = pytz.timezone('Asia/Tehran')
    try:
        df_old = pd.read_csv(file_name)
        last_date_data = df_old["Datetime"].values[-1]
        last_date_data = datetime.strptime(last_date_data, "%Y-%m-%d %H:%M:%S%z")
        temp_data = yf.Ticker(currency).history(period="1d", interval=interval).tz_convert(tz)
        last_online_date = temp_data["Close"].index[-1]
        if last_date_data < last_online_date:
            print("there is some new data")


        data = yf.Ticker(currency).history(period=period, interval=interval).tz_convert(tz)
        updated_data = df_old.append(data)
        updated_data.to_csv(file_name, mode='w', header=False)
    except:
        print("no data file")
        data = yf.Ticker(currency)
        df_old = data.history(period=period, interval=interval).tz_convert(tz)
        df_old.to_csv(file_name, mode='w', header=True)


create_data("5m")
