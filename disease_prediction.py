import streamlit as st
import numpy as np 
import pandas as pd 
import joblib
from streamlit_option_menu import option_menu

model1 = joblib.load("Diabetic_prediction.joblib")
model2 = joblib.load("Heart_prediction.joblib")
model3 = joblib.load("Parkinson_prediction.joblib")

st.set_page_config(layout="wide", 
                   page_title='Disease Prediction System',
                   page_icon=":sunglasses:",
                   initial_sidebar_state="expanded" )

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           [ 'Diabetes Prediction',
                             'Heart Disease Prediction',
                             'Parkinson Prediction'],
                             icons=['activity','heart', 'person'],
                             default_index=0,
                             )
# Pregnancies
# Glucose
# BloodPressure
# SkinThickness
# Insulin
# BMI
# DiabetesPedigreeFunction
# Age
if (selected == "Diabetes Prediction"):
    
    st.title("Diabetes Prediction  using ML")
    
    
    col1 , col2, col3 = st.columns(3)
   
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies")
   
    with col2:
         Glucose = st.number_input("Glucose Level")
    
    with col3:
         BloodPressure = st.number_input("Blood Pressure value")
            
    with col1:
         SkinThickness = st.number_input("Skin Thickness Value")
         
    with col2:
        Insulin = st.number_input("Insulin Level")
    
    with col3:
        BMI = st.number_input("BMI Value")
   
    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function Value")
    
    with col2:
         Age = st.number_input("Age")
    
    if st.button('Predict Diabetic'):
        
        input_data = np.array([[Pregnancies ,Glucose ,
                                BloodPressure ,SkinThickness ,
                                Insulin ,BMI , DiabetesPedigreeFunction , Age]])

        prediction = model1.predict(input_data)
        
        if prediction[0] == 1:
            st.error("The person is diabetic")  
        
        else:
            st.success("The person is not diabetic") 
            
# age,
# sex	,
# cp	,
# trestbps,
# chol,
# fbs,
# restecg,
# thalach,
# exang	,
# oldpeak	,
# slope	,
# ca,
# thal	
    
if (selected == "Heart Disease Prediction"):
    
    st.title("Heart Disease Prediction  using ML")
    
    
    # Input fields
    col1 , col2 , col3 = st.columns(3)
    with col1:  
        age = st.number_input("Age", min_value=0)
    with col2:
        sex = st.selectbox("Sex", ["Male", "Female"])
    with col3:
        cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    with col1:
        trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=0)
    with col2:
        chol = st.number_input("Serum Cholesterol in mg/dl (chol)", min_value=0)
    with col3:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
    with col1:
        restecg = st.selectbox("Resting ECG results (restecg)", [0, 1, 2])
    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=0)
    with col3:
        exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
    with col1:
        oldpeak = st.number_input("ST depression (oldpeak)", step=0.1)
    with col2:
        slope = st.selectbox("Slope of the peak exercise ST segment (slope)", [0, 1, 2])
    with col3:
        ca = st.selectbox("Number of major vessels (ca)", [0, 1, 2, 3, 4])
    with col1:
        thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

    # Map sex to numeric
    sex_numeric = 1 if sex == "Male" else 0

    # Predict button
    if st.button("Predict Heart Disease"):
        input_data = np.array([[age, sex_numeric, cp, trestbps, chol, fbs,
                                restecg, thalach, exang, oldpeak, slope, ca, thal]])
        prediction = model2.predict(input_data)

        if prediction[0] == 1:
            st.error("The person is likely to have Heart Disease.")
        else:
            st.success("The person is unlikely to have Heart Disease.")
    
#  MDVP:Fo(Hz)	,
# MDVP:Fhi(Hz),
# MDVP:Flo(Hz),
# MDVP:Jitter(%),
# MDVP:Jitter(Abs),
# MDVP:RAP	MDVP:PPQ,
#  Jitter:DDP	,
# MDVP:Shimmer	,
# MDVP:Shimmer(dB)	,
# Shimmer:APQ3,
# Shimmer:APQ5,
# MDVP:APQ,
# Shimmer:DDA,
# NHR,
# HNR,
# 	RPDE,
# DFA	,
# spread1,
# spread2,
# D2	,
# PPE   
    
if (selected == "Parkinson Prediction"):
    
    st.title("Parkinson's Disease Prediction using ML")

    # Input fields (grouped for readability)
    col1, col2 , col3 ,col4 , col5 = st.columns(5)

    with col1:
        fo = st.number_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.number_input("MDVP:Fhi(Hz)")
    with col3:   
        flo = st.number_input("MDVP:Flo(Hz)")
    with col4:    
        jitter_percent = st.number_input("MDVP:Jitter(%)")
    with col5:    
        jitter_abs = st.number_input("MDVP:Jitter(Abs)")
    with col1:    
        rap = st.number_input("MDVP:RAP")
    with col2:    
        ppq = st.number_input("MDVP:PPQ")
    with col3:    
        ddp = st.number_input("Jitter:DDP")
    with col4:    
        shimmer = st.number_input("MDVP:Shimmer")
    with col5:    
        shimmer_db = st.number_input("MDVP:Shimmer(dB)")
    with col1:    
        apq3 = st.number_input("Shimmer:APQ3")
    with col2:
        apq5 = st.number_input("Shimmer:APQ5")
    with col3:    
        apq = st.number_input("MDVP:APQ")
    with col4:    
        dda = st.number_input("Shimmer:DDA")
    with col5:    
        nhr = st.number_input("NHR")
    with col1:    
        hnr = st.number_input("HNR")
    with col2:    
        rpde = st.number_input("RPDE")
    with col3:    
        dfa = st.number_input("DFA")
    with col4:    
        spread1 = st.number_input("spread1")
    with col5:    
        spread2 = st.number_input("spread2")
    with col1:    
        d2 = st.number_input("D2")
    with col2:   
        ppe = st.number_input("PPE")

    # Predict button
    if st.button("Predict Parkinson's"):
        input_data = np.array([[fo, fhi, flo, jitter_percent, jitter_abs,
                                rap, ppq, ddp, shimmer, shimmer_db,
                                apq3, apq5, apq, dda, nhr, hnr,
                                rpde, dfa, spread1, spread2, d2, ppe]])
        
        prediction = model3.predict(input_data)

        if prediction[0] == 1:
            st.error("The person is likely to have Parkinson’s Disease.")
        else:
            st.success("The person is unlikely to have Parkinson’s Disease.")

    