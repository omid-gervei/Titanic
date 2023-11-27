# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 22:22:42 2023

@author: omidg
"""
import streamlit as st
import numpy as np
#import joblib
import pickle
#model = joblib.load('xgbpipe.joblib')
model = pickle.load(open('omid.pkl', 'rb'))
st.title('Will you survive if you were among Titanic passengers or not :ship:')
# PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
passengerid = st.text_input("Input Passenger ID", '8585') 
pclass = st.selectbox("Choose class", [1,2,3])
name  = st.text_input("Input Passenger Name", 'DR.Omid Gervei')
sex = st.selectbox("Sex 0 for Male 1 for female", [0,1])
age = st.slider("Choose age",0,100)
sibsp = st.slider("Choose siblings",0,10)
parch = st.slider("Choose parch",0,10)
ticket = st.text_input("Input Ticket Number", "8585") 
fare = st.number_input("Input Fare Price", 0,1000)
cabin = st.text_input("Input Cabin", "C52") 
embarked = st.selectbox("S=0 C=1 Q=2", [1,2,3])

def predict(): 
    row = np.array([pclass,sex,age,sibsp,parch,fare,embarked]) 
    row = row.reshape(1,7)
    prediction = model.predict(row)
    if prediction[0] == 1: 
        st.success('Passenger Survived :thumbsup:')
    else: 
        st.error('Passenger did not Survive :thumbsdown:') 

trigger = st.button('Predict', on_click=predict)