import numpy as np
import pandas as pd
import streamlit as st
from sklearn import svm

st.title('Cupcake Vs Muffins')
flour_quantity = st.slider('Slide to enter flour quantity:', 0, 500, 1)
sugar_quantity = st.slider('Slide to enter sugar quantity:', 0, 500, 1)

recipes = pd.read_csv('Cupcakes vs Muffins.csv')
type_label = np.where(recipes['Type'] == 'Muffin', 0, 1)
recipes_features = recipes.columns.values[1:].tolist()
ingredients = recipes[['Flour', 'Sugar']].values

# fit model
model = svm.SVC(kernel='linear')
model.fit(ingredients, type_label)


if st.button('Predict'):
    if (model.predict([[flour_quantity, sugar_quantity]])) == 0:
        st.success("You're scrolled to MUFFIN Recipe")
    else:
        st.success("You're looking to CUPCAKE Recipe")


