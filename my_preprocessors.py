import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin

#Clase para extraer el primer caracter de variable
class ExtractFirstCharacter(BaseEstimator, TransformerMixin):

    #Constructor
    def __init__(self, variables):
        if not isinstance(variables, list):
            raise ValueError("Las varibles debe ser incluida en una lista.")
        
        self.variables = variables
        
    #metodo fit para habilitar metodo transform
    def fit(self, X, y=None):
        return self

    #metodo para transformar variables temporales.
    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].str[0]
        return X