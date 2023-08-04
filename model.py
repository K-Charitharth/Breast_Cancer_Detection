import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def preprocess_data(data_file_name):
    # Read the data from the CSV file
    df = pd.read_csv('breast_cancer_detection.csv')
    df.replace('?', np.nan, inplace = True)
    df.dropna(inplace=True)
    df.drop(['id'], axis = 1, inplace = True)
    df['class'].replace(2,0, inplace = True)
    df['class'].replace(4,1, inplace = True)

    # Preprocess the dataset
    X = df.drop('class', axis=1)
    y = df['class']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    # Create and train the model
    rf_clf = RandomForestClassifier()
    rf_clf.fit(X_train, y_train)

    return rf_clf

def save_model(model, model_file):
    # Save the model to a file
    joblib.dump(model, model_file)
