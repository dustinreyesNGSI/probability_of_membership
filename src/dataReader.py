import os
import math
import numpy as np
import pandas as pd
import streamlit as st

from config.config import rank_reference_filename, rank_reference_cols, rank_reference_colnames

DATA_DIR = "./data"

class dataReader:
    """"
        Class of functions used for loading all kinds od dataframe needed for the app.
    """

    def __init__(self):
        pass

    @st.cache(persist=True)
    def load_rank_ref(self):
        """
            Loads the PNP_RANK_REF.csv from the data folder and converts ranks into lower case.
        """

        #load reference file
        rankref = pd.read_csv(
            os.path.join(DATA_DIR, rank_reference_filename),
            usecols=rank_reference_cols
            )
        #rename fields
        rankref = rankref.rename(columns=rank_reference_colnames)
        rankref['rank'] = rankref['rank'].str.lower()

        return rankref

    def load_uploaded_file(self, data_file):
        """
            Converts the uploaded file from the user into a pandas dataframe.
        """
        nrows = sum(1 for row in open(data_file, "r")) #count the number of rows in the file
        chunksize = math.ceil(nrows * 0.2) #take 20% of the total rows at a time
        df = pd.read_csv(data_file, chunksize=chunksize)
        df = pd.concat([c for c in df])

        return df
        
