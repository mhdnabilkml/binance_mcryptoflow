import requests
import pandas as pd
import time

def get_klines(symbol='BTCUSDT', interval='1h', start_time=None, end_time=None, limit=1000):
    url = f"https://data-api.binance.vision/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit  # max 1000
    }
    if start_time:
        params["startTime"] = int(start_time)
    if end_time:
        params["endTime"] = int(end_time)

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    return data

raw_data = get_klines(symbol="BTCUSDT", interval="1h")
print(raw_data)