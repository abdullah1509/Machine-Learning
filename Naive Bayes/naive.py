import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('spam.csv', encoding='latin-1')
df['spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

st.title('Naive Bayes SPAM Detection')
emails = st.text_input('Write Email to Predict')

X_train, X_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)

v = CountVectorizer()
X_train_cv = v.fit_transform(X_train.values)

model = MultinomialNB()
model.fit(X_train_cv, y_train)

X_test_cv = v.transform(X_test)

if st.button('Predict'):
    emails_count = v.transform([emails])
    predict = model.predict(emails_count)

    if predict:
        import streamlit as st

        st.markdown("""
        <style>
        .stSuccess {
            color: red;
            background-color: #FF0000;
            color: #21C354;
            margin: 0px 0px 1rem;
            border: red; 
            border-radius: 3px 3px 3px 3px;
            height: 60px;
            padding: 15px;
            font-family: "Source Sans Pro", sans-serif;
        }
        </style>
        <p class="stSuccess">It's a SPAM!!!</p>
        """, unsafe_allow_html=True)

    elif not predict:
        st.success("It's a Ham")

