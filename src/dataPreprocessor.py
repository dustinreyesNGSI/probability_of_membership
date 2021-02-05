import os
import numpy as np
import pandas as pd
import streamlit as st

from config.config import upload_cols, lbl_encoders
from src.dataReader import dataReader
from src.modelPredict import modelPredict
from src.modelPredict import 

class dataPreprocessor:
    def __init__(self, filename):
        dR = dataReader()
        self.uploaded_file = dR.load_uploaded_file(filename)
        self.rankref = dR.load_rank_ref()
        pass

    def add_reasons(self):
        self.uploaded_file['Reason'] = np.nan

    def validate_column_names(self):
        cols = self.uploaded_file.columns.tolist()
        assert cols == upload_cols, "The column names in the uploaded file do not match the expected names. \
            Expected {}, got {}".format(upload_cols, cols)

    def merge_ranks(self):
        df = self.uploaded_file.merge(
            self.rankref,
            on=['branch_of_service', 'rank'],
            how='left'
        )
        return df

    def validate_categorical(self, df):
        enc_dict = modelPredict().load_label_encoders()

    def get_df(self):
        self.add_reasons()
        return self.uploaded_file

    

    #validate cols
    #add column for reasons
    #validate rank
    #label encode
    #separate errors if any
    #return df


    
    