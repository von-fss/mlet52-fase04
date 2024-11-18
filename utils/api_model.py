import requests

def model_train(ticker: str) -> int:
    model_data = {'ticker':ticker}
    api_model = 'http://127.0.0.1:8000/models/train'
    # get = params
    response = requests.post(url=api_model, json=model_data)
    return response.status_code