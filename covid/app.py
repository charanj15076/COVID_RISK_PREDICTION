
import os
import requests
import streamlit as st
from src.train import Classifier
import math
import numpy as np
from utils import predict_json


def predict_class(USMER,MEDICAL_UNIT,SEX,PATIENT_TYPE,PNEUMONIA,AGE,PREGNANT,DIABETES,COPD,ASTHMA,INMSUPR,HIPERTENSION,OTHER_DISEASE,CARDIOVASCULAR,OBESITY,RENAL_CHRONIC,TOBACCO,CLASIFFICATION_FINAL):
    dt =  [list(map(int,[USMER,MEDICAL_UNIT,SEX,PATIENT_TYPE,PNEUMONIA,AGE,PREGNANT,
                                 DIABETES,COPD,ASTHMA,INMSUPR,HIPERTENSION,OTHER_DISEASE,
                                 CARDIOVASCULAR,OBESITY,RENAL_CHRONIC,TOBACCO,CLASIFFICATION_FINAL]))]



    cls = Classifier()
    return cls.load_and_test(dt)

def predict_class_gcp(USMER,MEDICAL_UNIT,SEX,PATIENT_TYPE,PNEUMONIA,AGE,PREGNANT,DIABETES,COPD,ASTHMA,INMSUPR,HIPERTENSION,OTHER_DISEASE,CARDIOVASCULAR,OBESITY,RENAL_CHRONIC,TOBACCO,CLASIFFICATION_FINAL):
    # Setup environment credentials (you'll need to change these)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "charanfinalproject1-e9e8c1c96999.json" # change for your GCP key
    PROJECT = "charanfinalproject1" # change for your GCP project
    REGION = "us-central1" # change for your GCP region (where your model is hosted)
    MODEL = "first_model"

    dt =  [list(map(int,[USMER,MEDICAL_UNIT,SEX,PATIENT_TYPE,PNEUMONIA,AGE,PREGNANT,
                                 DIABETES,COPD,ASTHMA,INMSUPR,HIPERTENSION,OTHER_DISEASE,
                                 CARDIOVASCULAR,OBESITY,RENAL_CHRONIC,TOBACCO,CLASIFFICATION_FINAL]))]
    
    covid = {
                0: 'ALive',
                1: 'DEAD',
            }

    preds = predict_json(project=PROJECT,
                         region=REGION,
                         model=MODEL,
                         instances=dt)

    return covid[preds[0]]

### Streamlit code (works as a straigtht-forward script) ###
st.title("Covid Classifier")
st.header("Classify Risk of covid")


#buttons on the web app

USMER = st.radio('Pick USMER',['0','1'])
MEDICAL_UNIT = st.radio('Pick MEDICAL_UNIT',['0','1'])
SEX = st.radio('Pick Gender',['0','1'])
PATIENT_TYPE = st.radio('Pick Patient_type',['0','1'])
PNEUMONIA = st.radio('Pneumonia Y/N',['0','1'])
AGE = st.slider('Pick ur Age', 0,100)
PREGNANT = st.radio('Pregnant Y/N',['0','1'])
DIABETES = st.radio('Diabetes Y/N',['0','1'])
COPD = st.radio('COPD Y/N',['0','1'])
ASTHMA = st.radio('Asthma Y/N',['0','1'])
INMSUPR = st.radio('INMSUPR Y/N',['0','1'])
HIPERTENSION = st.radio('HIPERTENSION Y/N',['0','1'])
OTHER_DISEASE = st.radio('OTHER_DISEASE Y/N',['0','1'])
CARDIOVASCULAR= st.radio('CARDIOVASCULAR Y/N',['0','1'])
OBESITY = st.radio('OBESITY Y/N',['0','1'])
RENAL_CHRONIC = st.radio('RENAL_CHRONIC Y/N',['0','1'])
TOBACCO =st.radio('TOBACCO Y/N',['0','1'])
CLASIFFICATION_FINAL = st.radio('CLASIFFICATION_FINAL Y/N',['0','1'])

# right = st.beta_columns(1)

if st.button("Predict GCP"):
    ret = predict_class(USMER, MEDICAL_UNIT, SEX, PATIENT_TYPE,PNEUMONIA,AGE,PREGNANT,DIABETES,COPD,ASTHMA,INMSUPR,
                           HIPERTENSION,OTHER_DISEASE,CARDIOVASCULAR,OBESITY,RENAL_CHRONIC,TOBACCO,CLASIFFICATION_FINAL)

    st.write(f"Prediction: {ret}")
    
    
# if st.button("Predict Local"):
#     conf_list = np.array(ret['log_proba'][0])
#     conf = math.exp(conf_list.max())*100

#     st.write(f"Prediction: {ret['prediction'][0]}")
#     st.write(f"Confidence: {conf:.2f}%")

