import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def wrangle_religion():
    """
    This is to bring in our US Religion Census data from 2010
    """
    df = pd.read_excel("U_S_Religion_Census_2010 _clean_data.xlsx")
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace(",", "")
    return df