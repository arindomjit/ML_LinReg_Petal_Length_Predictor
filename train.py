import seaborn as sns
from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib
import os

#Load dataset
data = sns.load_dataset("iris")

X = data.petal_width.to_numpy()
X = X.reshape(-1,1)

#Fit the model
lm = LinearRegression()
lm.fit(X, data.petal_length)

os.makedirs('model', exist_ok=True)
joblib.dump(value=lm, filename='model/linear_regression.pkl')

print("Model .pkl file generated")