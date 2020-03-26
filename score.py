import pandas as pd
import joblib

def predict_length(petal_width):
    
    #Load the model file
    lm=joblib.load('model/linear_regression.pkl')

    #petal_width = int("2")
    petal_width = int(petal_width)
    
    prediction_data = pd.DataFrame( { 'petal_width': [petal_width] } )
    result = lm.predict(prediction_data)
    return result