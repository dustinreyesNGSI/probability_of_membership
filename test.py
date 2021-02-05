from src.dataReader import dataReader
from src.dataPreprocessor import dataPreprocessor
import pandas as pd

dPre = dataPreprocessor('./data/actual.csv')
n, r = dPre.get_model_df()
print(n.head())