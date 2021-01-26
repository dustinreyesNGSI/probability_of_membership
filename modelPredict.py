import os
import numpy as np
import pandas as pd
import xgboost as xgb
import pickle
import streamlit as st

from sklearn.preprocessing import LabelEncoder

class modelPredict:
    def __init__(self):
        pass
    
    def load_model(self):
        #load XGBOOST model
        xgbmodel = pickle.load(open("models/xgboost_pom.pickle.dat", "rb"))

        #load sklearn label encoders
        lbl_rank = pickle.load(open("models/rank_lblenc", "rb"))
        lbl_bos = pickle.load(open("models/real_bos_lblenc", "rb"))
        lbl_type = pickle.load(open("models/type_lblenc", "rb"))

        return xgbmodel, lbl_rank, lbl_bos, lbl_type

    def validate_data(self):
        pass