import streamlit as st
import pandas as pd
from streamlit_help.get_data import get_data

st.set_page_config(
    page_title="Nvdia timeline"
)

appTitleSubtitle = ["# Finance Data","NVDIA 5 Days period"]
st.write(f"""
{appTitleSubtitle[0]}
{appTitleSubtitle[1]}
""")
    
# Creating dataframe
# Get data from API

# import yfinance as yf
# nvda = yf.Ticker("NVDA")

############

#plot
st.line_chart(get_data()['Close'])