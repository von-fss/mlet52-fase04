import streamlit as st
from utils.api_model import model_train
# import pandas as pd

appTitleSubtitle = ["# Finance Data","NVDIA 5 Days period"]

st.write(f"""
{appTitleSubtitle[0]}
{appTitleSubtitle[1]}
""")
    
if st.button("Model Train", type="primary"):
    st.write("NVDA Trained", " - ", "Status ", model_train('NVDA'))
else:
    st.write("Last model - 24h ago")
