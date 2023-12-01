# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:16:25 2023

@author: omidg
"""

import gradio as gr
import pickle
def make_prediction(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked):
    with open("omid.pkl", "rb") as f:
        clf  = pickle.load(f)
        preds = clf.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
    if preds == 1:
            return "He will survive"
    return "He will ot survive"

#Create the input component for Gradio since we are expecting 4 inputs

Pclass_input = gr.Number(label = "PClass:1,2,3")
Sex_input = gr.Number(label= "Male:1 , Female:0")
Age_input = gr.Number(label = "Age")
SibSp_input = gr.Number(label = "SibSp")
parch_input = gr.Number(label = "parch")
Fare_input = gr.Number(label = "Fare")
Embarked_input = gr.Number(label = "Embarked")
# We create the output
output = gr.Textbox()


app = gr.Interface(fn = make_prediction, inputs=[Pclass_input,Sex_input, Age_input, SibSp_input, parch_input,Fare_input,Embarked_input], outputs=output)
app.launch()