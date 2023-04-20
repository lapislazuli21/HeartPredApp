# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:02:22 2023

@author: Khush
"""

import json
import requests

url = 'http://127.0.0.1:8000/heart_disease_prediction'

model_input_data = {
    
    'Age': 48,
    'Sex': 1,
    'CP': 4,
    'BP': 122,
    'Cholesterol': 222,
    'FBS': 0,
    'EKG': 2,
    'MaxHR': 186,
    'Exang': 0,
    'STdep': 0,
    'SlopeST': 1,
    'NumVessel': 0,
    'Thallium': 3
    
    }
    
input_json = json.dumps(model_input_data)

response = requests.post(url, data=input_json)

print(response.text)    