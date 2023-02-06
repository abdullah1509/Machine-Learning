import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('iris.csv')

st.title('Random Forest Classifier')

X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']

model = RandomForestClassifier(n_jobs=2, random_state=0)
model.fit(X, y)

sepal_len = st.slider('Scroll to set Sepal Langth', 0.0, 10.0)
sepal_wid = st.slider('Scroll to set Sepal Width', 0.0, 5.0)
petal_len = st.slider('Scroll to set Petal Length', 0.0, 10.0)
petal_wid = st.slider('Scroll to set Petal Width', 0.0, 5.0)

input_feature = np.array([[sepal_len, sepal_wid, petal_len, petal_wid]])

output = model.predict(input_feature)

if st.button('Predict'):
    if output == ['setosa']:
        st.success('Setosa')

    elif output == ['versicolor']:
        st.success('Versicolor')

    elif output == ['virginica']:
        st.success('Virginica')