from flask import Flask, jsonify, request
import pandas as pd
import numpy as np

import config_titanic as cfg
import pp_predict_titanic as pp
import json
from json import JSONEncoder

app = Flask(__name__)

# Funcion para convertir json
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

#ruta para predecir.
@app.route("/prediccion_titanic", methods=['POST'])
def predict_from_pp():
    json_data = request.get_json()
    dataframe = pd.json_normalize(json_data)
    data = dataframe

    #prediccion
    data = data[cfg.FEATURES] # Se seleccionan solo las variables a utilizar en el modelo
    data['Pclass'] = data['Pclass'].astype('O') # Parseo de variable Pclass a categorica
    data = data.replace(r'^\s*$', np.NaN, regex=True) # Sustitución de datos vacios por NaN
    resultado = pp.predict(data)
    numpyData = {"resultado": resultado} #Generacion de diccionario para codificar a json
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # escribir arreglo a archivo json
    print(encodedNumpyData)
    return encodedNumpyData

