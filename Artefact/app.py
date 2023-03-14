import streamlit as st
from predict_page import show_preditic_page
from explore_page import show_exp_page


page = st.sidebar.selectbox('Chose the page', ('Predictive system','Exploratory Data Analysis','ARU Current Insights'))
if page == 'Predictive system':
    show_preditic_page()
else:
    show_exp_page()
