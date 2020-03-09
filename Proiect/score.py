import json
import numpy as np
from azure.core.model import Model
from sklearn.externals import joblib

def init():
    global model
    model_path = Model.get_model_path('lightGBM')
    model = joblib.load(model_path)
    
def run(raw_data):
    try:
        data = json.loads(raw_data)['value']
        X = np.array(data)
        y = model.predict(X)
        return json.dumps({"result": y.tolits()})
    
    except Exception as e:
        error = str(e)
        return error