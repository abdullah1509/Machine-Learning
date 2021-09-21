import streamlit as st
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.title('Machine Learning Project')

dataset_name = st.sidebar.selectbox('Select Dataset', ('Iris', 'Breast Cancer', 'Wine'))

st.write(f"## {dataset_name} Dataset")

classifier_name = st.sidebar.selectbox('Select classifier', ('KNN', 'SVM', 'Random Forest'))

def get_dataset(name):
    data = None
    if name == 'Iris':
        data = datasets.load_iris()
    elif name == 'Wine':
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()
    X = data.data
    y = data.target
    return X, y

X, y = get_dataset(dataset_name)
st.write('Shape of dataset:', X.shape)
st.write('number of classes:', len(np.unique(y)))

def add_parameter_ui(model_name):
    params = dict()
    if model_name == 'SVM':
        C = st.sidebar.slider('C', 0.01, 10.0)
        params['C'] = C
    elif model_name == 'KNN':
        K = st.sidebar.slider('K', 1, 15)
        params['K'] = K
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 15)
        params['max_depth'] = max_depth
        n_estimators = st.sidebar.slider('n_estimators', 1, 100)
        params['n_estimators'] = n_estimators
    return params

params = add_parameter_ui(classifier_name)

def get_classifier(model_name, params):
    model = None
    if model_name == 'SVM':
        model = SVC(C=params['C'])
    elif model_name == 'KNN':
        model = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        model = RandomForestClassifier(n_estimators=params['n_estimators'],
            max_depth=params['max_depth'], random_state=1234)
    return model

model = get_classifier(classifier_name, params)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)

st.write(f'Classifier = {classifier_name}')
st.write(f'Accuracy =', acc)
