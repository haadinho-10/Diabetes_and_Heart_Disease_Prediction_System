# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:28:26 2023

@author: batha
"""
import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes=pickle.load(open('C:/Users/batha/OneDrive/Desktop/mlprojects/trainedmodel.sav','rb'))

heart=pickle.load(open('C:/Users/batha/OneDrive/Desktop/mlprojects/heart.sav','rb'))


#sidebar for navigation

with st.sidebar:
    selected= option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction'],default_index=0)


#Diabetes prediction page

if (selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    #input parameters
    Pregnancies=st.text_input('No of pregnancies')
    Glucose=st.text_input('Blood Glucose level')
    BP=st.text_input('Blood Pressure value')
    SkinThickness=st.text_input('skin thickness value')
    insulin=st.text_input('insulin level')
    BMI=st.text_input('bmi')
    Diabetespedigreefunction=st.text_input('Diabetespedigree function value')
    age=st.text_input('enter age')
    
    #code for prediction
    diagnosis=''
    
    if st.button('Diabetes Test result'):
        diab_predict=diabetes.predict([[Pregnancies,Glucose,BP,SkinThickness,insulin,BMI,Diabetespedigreefunction,age]])
        if (diab_predict[0] == 1):
            diagnosis='The person is diabetic'
        else:
            diagnosis='The person is not diabetic'
    st.success(diagnosis)


if (selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')

    

                                                               
