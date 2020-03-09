import datetime
from dateutil.tz import tzutc
import pandas as pd
import dtFeatures as dtF
from sklearn.metrics import mean_squared_error
from azureml.core import Experiment, Run, Workspace, Model
from lightgbm import LGBMRegressor
from math import sqrt
import joblib
import train_Data as td
import os

def split_data(X,y, test_size = 0.2):
    n = len(X.index)
    return(X.iloc[:int((1-test_size)*n)], X.iloc[int((1-test_size)*n):n], y.iloc[:int((1-test_size)*n)], y.iloc[int((1-test_size)*n):n])