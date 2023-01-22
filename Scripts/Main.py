import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import schedule
import time
# import talib

# data = yf.download(tickers='EURUSD=X', period='1y', interval='1mo')
# ichimoku = Ichimoku.Ichimoku(data, 9, 26, 52, 26)
# tenken_sen = ichimoku.create_data()
# fig = go.Figure()
#
# fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
#                              name='Market Data'))
# fig.add_trace(go.Scatter(x=data.index, y=tenken_sen, line=dict(color='blue', width=1.5), name='tenken'))
#
# fig.update_layout(title='EUR-USD')
#
# fig.show()
#
# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])
#
# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter


# Initialize the app
app = dash.Dash()

# Define the layout of the app
app.layout = html.Div([dcc.Graph(id='forex-chart')])


# Define a function to update the chart
def update_chart():
    # Get the data
    data = yf.download(tickers='EURUSD=X', period='1y', interval='1mo')

    # Create the chart
    # tenkan_sen = talib.SMA(data['High'], timeperiod=9)
    # kijun_sen = talib.SMA(data['Low'], timeperiod=26)
    # senkou_span_a = (tenkan_sen + kijun_sen) / 2
    # senkou_span_b = talib.SMA(data['Close'], timeperiod=52)
    # chikou_span = data['Close'].shift(26)

    # Plot the lines on the chart
    chart = go.Candlestick(x=data.index,
                           open=data['Open'],
                           high=data['High'],
                           low=data['Low'],
                           close=data['Close'])
    # chart.add_trace(go.Scatter(x=data.index, y=tenkan_sen, name='Tenkan-sen'))
    # chart.add_trace(go.Scatter(x=data.index, y=kijun_sen, name='Kijun-sen'))
    # chart.add_trace(go.Scatter(x=data.index, y=senkou_span_a, name='Senkou Span A'))
    # chart.add_trace(go.Scatter(x=data.index, y=senkou_span_b, name='Senkou Span B'))
    # chart.add_trace(go.Scatter(x=data.index, y=chikou_span, name='Chikou Span'))

    fig = go.Figure(data=[chart])

    # Show the chart
    fig.show()
    # Update the chart
    app.callback(
        Output('forex-chart', 'figure'),
        [Input('interval-component', 'n_intervals')])(chart)


# Schedule the function to run every 10 seconds
schedule.every(10).seconds.do(update_chart)

# Start the app
if __name__ == '__main__':
    app.run_server(debug=true,)

# keep running the scheduled task
while True:
    schedule.run_pending()
    time.sleep(1)
