import streamlit as st
import pandas as pd
import requests 
import altair as alt
import boto3
import re 



st.title("Page to view data ")
containerFilter = st.container(height=100, border=False)
containerChart = st.container(height=600, border=False) 


def loadDataPredicted():
    #print chart with the ticker value    
    with containerChart:
        result =  st.session_state['name']    
        if result != None:
            print(result)
            server_api_getHistory: str = f'http://127.0.0.1:8000/yfinance/getHistory/?ticker={result}'
            response = requests.get(server_api_getHistory)
            lstHistory = pd.DataFrame(response.json())
            lstHistory['Type']= 'Closed'

            server_api_predict: str = f'http://127.0.0.1:8000/models/predict?ticker={result}'
            response = requests.get(server_api_predict)

            tmpDf = pd.DataFrame([{'Date': "Predicted", 'Close': response.json()['predicted'], 'Type': 'Prediction' }])
            lstHistory = pd.concat([lstHistory, tmpDf])
            

            chart_data = pd.DataFrame({'Date': lstHistory['Date'], 
                                    'Value': lstHistory['Close'].round(0),
                                    'Type': lstHistory['Type']})
            print(chart_data)
            st.write('Here is the history of stock value')
            #st.scatter_chart(chart_data, y=['Value', 'Predicted'], x='Date', x_label='', y_label='' , height=550, use_container_width=True, color=["#FF0000", "#0000FF"])
            c = (
                alt.Chart(chart_data, height=300, width=700)
                .mark_line(point=True)
                .encode(
                    alt.X('Date'), 
                    alt.Y('Value').axis(None), 
                    alt.Color('Type'))
            )
            
            labels = c.mark_text(dx=0, dy=-10, align='center').encode(text='Value')
            #st.altair_chart(c, labels, use_container_width=True)
            c + labels


with containerFilter:

    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket='modeldataqbase', StartAfter='model/')
    
    
    lstTickers = pd.DataFrame(columns=['name'])
    if 'Contents' in response:
        for obj in response['Contents']:
            
            dfObj = pd.DataFrame({'name': [''.join(re.findall('/(.*)\.', obj['Key']))]})
            lstTickers = pd.concat([lstTickers, dfObj])
    else:
        print("No files found in the bucket.")    
    
    result = st.selectbox("Select a Ticker to estimate the future value", lstTickers[['name']], key='name', on_change=loadDataPredicted)
