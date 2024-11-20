import streamlit as st
import pandas as pd
from streamlit_help.get_data import get_data
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.chart_container import chart_container
import boto3

st.set_page_config(
    page_title="Stock Market"
)


pg = st.navigation([st.Page('streamlit_dataviz.py', title='Dataviz'),
                    st.Page('streamlit_trainmodel.py', title='Trainnig Model')])
pg.run()