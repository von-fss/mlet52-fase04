import streamlit as st
import pandas as pd
import requests 
import altair as alt
import boto3
import re 

st.title("Page to train model")

server_api_address =  "http://127.0.0.1:8000/yfinance/tickers"

response = requests.get(server_api_address)
lstTickers = pd.DataFrame(response.json())

lstPeriod = pd.DataFrame({'name': ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']})


with st.form("formTrain"):
    col1, col2 = st.columns(2)    
    ticker = col1.selectbox("Select a Ticker train !", lstTickers[['name']])
    epochs = col1.number_input("Epoch", value=20, min_value=1, max_value=100)
    learningRate = col1.number_input("Learning Rate", value=0.05, min_value=0.05, max_value=0.5)
    layers = col1.number_input("Layers", value=2, min_value=1, max_value=10)

    period = col2.selectbox(f"Period", lstPeriod[['name']], index=3)
    batchSize = col2.number_input("Batch Size", value=15, min_value=1, max_value=50)
    maxUnit = col2.number_input("Max Unit", value=100, min_value=20, max_value=200)
    submitted  = col2.form_submit_button(label="Train!!")



if submitted:
    with st.spinner(text="In progress..."):
        server_api_predict: str = f'http://127.0.0.1:8000/models/train'
        body = {
            "ticker": ticker,
            "time_step": 5,
            "epochs": epochs,
            "optimizer": "adam",
            "batch_size": batchSize,
            "learning_rate": learningRate,
            "nn_activation": "relu",
            "nn_max_units": maxUnit,
            "nn_layers": layers,
            "nn_return_sequences": "True",
            "loss": "mean_squared_error",
            "dropout": "True",
            "dropout_value": 0.2,
            "period": period
        }

        
        response = requests.post(url=server_api_predict, json=body)       

        if response.status_code == 200:
            st.success('Concluido')
        else:
            st.error(f'{response.status_code} - {response.text}')
            
        
        