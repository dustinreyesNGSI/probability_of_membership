import os
import numpy as np
import pandas as pd
import xgboost as xgb
import pickle
import streamlit as st

from sklearn.preprocessing import LabelEncoder
from config.config import upload_cols, lbl_encoders

class modelPredict:
    def __init__(self):
        pass
    
    def load_model(self):
        #load XGBOOST model
        model = pickle.load(open("models/xgboost_pom.pickle.dat", "rb"))
        return model

    def load_label_encoders(self):
        cols = upload_cols[:-1]
        encs = lbl_encoders
        enc_dict = {}

        #load sklearn label encoders
        for col, enc in zip(cols, encs):
            enc_dict[col] = pickle.load(open(enc, "rb"))
        return enc_dict
        