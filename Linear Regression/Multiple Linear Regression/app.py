import math
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import linear_model

data= pd.read_csv('home_price.csv')

median_bedroom= math.floor(data.Bedroom.median())
data.Bedroom= data.Bedroom.fillna(median_bedroom)

# Regression
reg= linear_model.LinearRegression()
reg.fit(data[['Area', 'Bedroom', 'Age']], data.Price)
r2_score= reg.score(data[['Area', 'Bedroom', 'Age']], data.Price)


st.markdown('# Housing Price')
area = st.number_input('Enter the Area', 0)
bed_num = [1,2,3,4,5,6]
bedroom = st.selectbox('Enter the number of BedRoom', bed_num)
#bedroom = st.slider('Enter the number of BedRoom ', 0, 10, 0)
age = st.slider('How old the house is ', 0, 20, 0)


input_features = np.array([[area, bedroom, age]])
# Area, BedRoom, Age
prediction = reg.predict(input_features)

if st.button('Submit'):
    st.write(prediction)
    st.write('Accuracy ', r2_score)
