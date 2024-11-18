import requests
import pandas as pd


def get_data():
    url = "http://127.0.0.1:8000/yfinance"
    response = requests.get(url)
    json_data = response.json()
    df = pd.DataFrame(json_data)
    
    ## Create index
    df.set_index('Date', inplace=True)

    return df