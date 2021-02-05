import os
import numpy as np
import pandas as pd
import streamlit as st

from config.config import upload_cols, lbl_encoders
from src.dataReader import dataReader
from src.modelPredict import modelPredict

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
        cols = list(enc_dict.keys())
        temp_df = df[cols].copy()

        print(enc_dict.get('rank').classes_)
        #create a binary dataframe to check if each labels exist in the LabelEncoder classes_
        for col in cols:
            # temp_df[col] = temp_df[col].apply(lambda x: x in enc_dict.get(col).classes_)
            temp_df[col] = temp_df[col].isin(enc_dict.get(col).classes_)

        #get indices where there are nulls
        null_ind = temp_df.isna().sum(1).index.tolist()
        if len(null_ind) == 0:
            null_ind = [-99] #dummy
        indices = []
        for i in temp_df.index.tolist():
            if i not in null_ind:
                indices.append(i)

        del temp_df, null_ind
        return indices

    def get_model_df(self):
        # self.add_reasons()
        try:
            self.validate_column_names()
        except AssertionError as e:
            raise e

        df = self.merge_ranks()
        print('ranks')
        indices = self.validate_categorical(df)
        print('categorical')
        new_df = df.iloc[indices, :].copy()

        #if there are rejects found
        if len(indices) != df.shape[0]:
            rj_ind = []
            for i in df.index.tolist():
                if i not in indices:
                    rj_ind.append(i)
            rejects_df = df.iloc[indices, :].copy()

            return new_df, rejects_df
        return new_df, None

    #validate cols
    #add column for reasons
    #validate rank
    #label encode
    #separate errors if any
    #return df


    
    