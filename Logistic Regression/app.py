import pandas as pd
import numpy as np
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('spam.csv', encoding='latin-1')
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
df.rename(columns = {'v1':'Category', 'v2':'Message'}, inplace = True)
df['spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

st.title('Logistic Regression')
emails = st.text_input('Write Email to Predict')

X_train, X_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)

v = CountVectorizer()
X_train_cv = v.fit_transform(X_train.values)

model=LogisticRegression()
model.fit(X_train_cv, y_train)

X_test_cv = v.transform(X_test)

if st.button('Predict'):
    emails_count = v.transform([emails])
    predict = model.predict(emails_count)

    if predict == True:
        st.write("It's a SPAM!!!")

    elif predict == False:
        st.write("It's a Ham")
