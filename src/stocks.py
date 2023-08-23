import requests
import matplotlib.pyplot as plt
from datetime import datetime

API_KEY_PATH = 'apikey.txt'

def read_apikey(filepath: str = API_KEY_PATH ) -> str:
    with open(filepath) as f: lines = f.readlines()
    return lines[0] 


def get_historical_stock_data(symbol):
    endpoint = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': read_apikey(),
    }
    response = requests.get(endpoint, params=params)
    data = response.json()

    dates = []
    prices = []

    for date, values in data['Time Series (Daily)'].items():
        dates.append(date)
        prices.append(float(values['4. close']))
    
    return dates[::-1], prices[::-1]

def plot_stock_prices(symbol, dates, prices):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, prices, marker='o')
    plt.title(f'Historical Stock Prices for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

stock_symbol = 'AAPL'
dates, prices = get_historical_stock_data(stock_symbol)
plot_stock_prices(stock_symbol, dates[-50:], prices[-50:])