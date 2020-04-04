import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split

def split_my_data(df):
    return train_test_split(df, train_size=.80, random_state=123)


def plot_corr_heatmat(df, color='Purples'):
    """
    Takes in a dataframe and returns a heatmap of the correlations
    """
    plt.figure(figsize=(10,10))
    sns.heatmap(df.corr(), cmap=color, annot=True)

def plot_variable_pairs(df):
    """
    This function returns a pairplot to help explore relationships
    """
    plt.figure(figsize=(10,10))
    sns.pairplot(df, kind="reg", plot_kws={"line_kws":{"color":"purple"}, "scatter_kws":{"alpha": 0.5}})