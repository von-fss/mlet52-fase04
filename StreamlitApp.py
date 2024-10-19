import streamlit as st
import pandas as pd


appTitleSubtitle = ["# Finance Data","NVDIA 5 Days period"]

st.write(f"""
{appTitleSubtitle[0]}
{appTitleSubtitle[1]}
""")
    
# Creating dataframe
import yfinance as yf
nvda = yf.Ticker("NVDA")

#df = pd.read_csv("my_data.csv")
st.line_chart(nvda.history(period="5d")["Close"])