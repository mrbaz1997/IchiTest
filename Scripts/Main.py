import pandas
import yfinance as yf
import pandas as pd
import time
import pytz
from datetime import datetime


def create_data(interval, currency="EURUSD=X", period="5d"):
    file_name = "CachedData/" + currency + "_" + interval
    tz = pytz.timezone('Asia/Tehran')
    try:
        df_old = pd.read_csv(file_name)
        print(df_old)
        last_date_data = df_old["Datetime"].values[-1]
        last_date_data = datetime.strptime(last_date_data, "%Y-%m-%d %H:%M:%S%z")
        temp_data = yf.Ticker(currency).history(period="1d", interval=interval).tz_convert(tz)
        last_online_date = temp_data["Close"].index[-1]
        if last_date_data < last_online_date:
            print("there is some new data")
            diff_x = 0
            for x in reversed(temp_data.index):
                if last_date_data >= x:
                    break
                diff_x += 1

            temp_data.tail(diff_x).to_csv(file_name+"_temp", mode='w', header=True)
            temp_data = pd.read_csv(file_name+"_temp")
            # print(temp_data)
            updated_data = pd.concat([df_old, temp_data.tail(diff_x)], ignore_index=True)

        # data = yf.Ticker(currency).history(period=period, interval=interval).tz_convert(tz)
        # updated_data = df_old.append(data)
        updated_data.to_csv(file_name, mode='w', header=True, index=False)
    except:
        print("no data file")
        data = yf.Ticker(currency)
        df_old = data.history(period=period, interval=interval).tz_convert(tz)
        print(df_old)
        df_old.to_csv(file_name, mode='w', header=True)
        df_old = pd.read_csv(file_name)
        print(df_old)
        df_old.to_csv(file_name, mode='w', header=True, index=False)
        df_old = pd.read_csv(file_name)
        print(df_old)


create_data("5m")
