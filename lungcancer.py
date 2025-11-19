# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 11:44:05 2025

@author: rudra
"""

import pickle
import streamlit as st
import pandas as pd
pipe=pickle.load(open("C:/Users/rudra/Downloads/lungcancer.pkl","rb"))


st.title("LungCancer Detection App Made By Rudra")
html_temp="""
<div style="background-color:cyan;padding:5px",width:400px;height:200px">
<h2 style="color:black;text-align:center;">Check LungCancer</h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
st.text("")



st.sidebar.markdown(
    """
    <div style="background-color:white;padding:5px",width:400px;height:400px">
    <h2 style='color:black;font-size:28px;text-align:center;'>Enter Patient Details</h2>
    
    """,unsafe_allow_html=True)


GENDER=st.sidebar.selectbox('Enter Gender',['M','F'])
AGE=st.sidebar.number_input('Enter Age')
SMOKING=st.sidebar.number_input('Enter SMOKING')
YELLOW_FINGERS=st.sidebar.number_input('Enter YELLOW_FINGERS')
ANXIETY=st.sidebar.number_input('Enter ANXIETY')
PEER_PRESSURE=st.sidebar.number_input('Enter PEER_PRESSURE')
CHRONIC_DISEASE=st.sidebar.number_input('Enter CHRONIC_DISEASE')
FATIGUE=st.sidebar.number_input('Enter FATIGUE')
ALLERGY=st.sidebar.number_input('Enter ALLERGY')
WHEEZING=st.sidebar.number_input('Enter WHEEZING')
ALCOHOL_CONSUMING=st.sidebar.number_input('Enter ALCOHOL_CONSUMING')
COUGHING=st.sidebar.number_input('Enter COUGHING')
SHORTNESS_OF_BREATH=st.sidebar.number_input('Enter SHORTNESS_OF_BREATH')
SWALLOWING_DIFFICULTY=st.sidebar.number_input('Enter SWALLOWING_DIFFICULTY')
CHEST_PAIN=st.sidebar.number_input('Enter CHEST_PAIN')


if st.button("Predict LungCancer "):
    
    input_df=pd.DataFrame({
        "GENDER":[GENDER],
        "AGE":[AGE],
        "SMOKING":[SMOKING],
        "YELLOW_FINGERS":[YELLOW_FINGERS],
        "ANXIETY":[ANXIETY],
        "PEER_PRESSURE":[PEER_PRESSURE],
        "CHRONIC_DISEASE":[CHRONIC_DISEASE],
        "FATIGUE":[FATIGUE],
        "ALLERGY":[ALLERGY],
        "WHEEZING":[WHEEZING],
        "ALCOHOL_CONSUMING":[ALCOHOL_CONSUMING],
        "COUGHING":[COUGHING],
        "SHORTNESS_OF_BREATH":[SHORTNESS_OF_BREATH],
        "SWALLOWING_DIFFICULTY":[SWALLOWING_DIFFICULTY],
        "CHEST_PAIN":[CHEST_PAIN]})
    prediction=pipe.predict(input_df)
    if prediction[0]==1:
        st.header('Patient Has LungCancer')
    
    else:
        st.error('Patient Has No LungCancer')

        
