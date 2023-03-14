from ast import Expression
from os import fstat
from tkinter import Button
import streamlit as st
import pickle
import numpy as np 

def load_model():
    with open("cl_model.pkl","rb") as file:
        saved_cl_model = pickle.load(file)
    with open("r_model.pkl","rb") as file:
        saved_r_model = pickle.load(file)
    return saved_cl_model,saved_r_model

saved_cl_model,saved_r_model = load_model()

def show_preditic_page():
    st.title("Graduate Admission Predictor")


    GRE = st.slider('GRE Score', 260,340,300)
    TOEFL = st.slider('TOEFL Score', 0,120,100)

    Rank = st.selectbox(
     'Course Ranking',
     (1,2,3,4,5), index=4)
    SOP = st.slider('SOP', 1,5,4)
    LOR = st.slider('LOR', 1,5,5)


    CGPA = st.number_input('Enter CGPA', max_value= 10.00, value=8.00)
    

    selectbox = st.selectbox(
     'Have student conducted a research before?',
     ('Yes', 'No'))
    if selectbox == 'Yes':
        Research = 1
    else:
        Research = 0

    ok = st.button('Predict')
    if ok:
        pred = np.array([[GRE,TOEFL,Rank,SOP,LOR,CGPA,Research]])
        saved_cl_model.predict(pred) 
        saved_r_model.predict(pred)
        y_pred_cl = saved_cl_model.predict(pred)
        y_pred_r = saved_r_model.predict(pred)
        if y_pred_cl[0]==0:
            decision = 'Application is not good'
        else:
            decision='Application is good'
        pred2 = int(y_pred_r[0]*100)

        
        st.subheader(f"Application prediction is: {decision}")
        st.caption("Classification machine model")
        st.subheader(f"Admission Chance is: {pred2} %")
        st.caption("Regression machine model")

