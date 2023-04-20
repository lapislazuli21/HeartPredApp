# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:01:02 2023

@author: Khush
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    
    Age: int
    Sex: int
    CP: int
    BP: int
    Cholesterol: int
    FBS: int
    EKG: int
    MaxHR: int 
    Exang: int
    STdep: float 
    SlopeST: int
    NumVessel: int
    Thallium: int
    
    
pred_model = pickle.load(open('prediction_model.sav', 'rb'))

@app.post('/heart_disease_prediction')
def heart_pred(input_parameters: model_input):
    
    input_data = input_parameters.json()
    input_dict = json.loads(input_data)
    
    age = input_dict['Age']
    sex = input_dict['Sex']
    cp = input_dict['CP']
    bp = input_dict['BP']
    chol = input_dict['Cholesterol']
    fbs = input_dict['FBS']
    ekg = input_dict['EKG']
    maxhr = input_dict['MaxHR']
    exang = input_dict['Exang']
    stdep = input_dict['STdep']
    slopest = input_dict['SlopeST']
    numvessel = input_dict['NumVessel']
    thal = input_dict['Thallium']
    
    input_list = [age, sex, cp, bp, chol, fbs, ekg, maxhr, exang, stdep, slopest, numvessel, thal]
    
    prediction = pred_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'You may not have Heart Disease.'
    else:
        return 'You may have Heart Disease!'