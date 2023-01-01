import streamlit as st
import pandas as pd
from sklearn import linear_model

data= pd.read_csv('price.csv')
price= data.Price
new_data= data.drop('Price', axis='columns')

# Regression
reg= linear_model.LinearRegression()
reg.fit(new_data, price)

r2_score= reg.score(new_data, price)


st.markdown('# Housing Price')

area = st.number_input('Enter the Area', 0)


if st.button('Submit'):
    prediction = reg.predict([[area]])
    st.write(prediction)
    st.write('Accuracy', r2_score)

    
