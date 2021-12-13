import joblib
import config_titanic as cfg
import pandas as pd
import numpy as np

#Cargamos modelo y pipeline
Titanic_model = joblib.load('Titanic_pipeline.pkl')

#Funcion.
def predict(X):
    predicts = Titanic_model.predict(X)
    salida = predicts
    print(salida)
    return salida

#Test = pd.read_csv('test.csv')
#Test = Test[cfg.FEATURES]
#preds = predict(Test)
#print(preds)