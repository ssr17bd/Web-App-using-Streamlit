# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:13:00 2020

@author: Shaila Sarker
"""

import pandas as pd
import streamlit as st
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App

This app predicts the **Iris Flower** type
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 7.9)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.9)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)
    data = {'Sepal Length': sepal_length,
            'Sepal Width': sepal_width,
            'Petal Length': petal_length,
            'Petal Width': petal_width}
    features = pd.DataFrame(data, index = [0])
    return features

df = user_input_features()

# print out the user inputs in the main body
st.subheader('User Input parameters')
st.write(df)

#load iris dataset
iris = datasets.load_iris()
X = iris.data #assign 4 features (sepal_length...petal_width) into X variable
Y = iris.target #class index numbers (0, 1, 2) with the class labels (setosa, versicolor, virginica) [will be shown in the output]

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

#print the class labels and corresponding index numbers
st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

# print the class label 
st.subheader('Prediction')
st.write(iris.target_names[prediction])

# print the probablity with corresponding index numbers of the class labels
st.subheader('Prediction Probability')
st.write(prediction_proba)
