from src.dataReader import dataReader
from src.dataValidation import dataValidation
import pandas as pd

dV = dataValidation('./data/actual.csv')
print(dV.get_df().head())
