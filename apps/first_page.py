# Importing the required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import streamlit as st

def app():
    st.title("Access Data")

    st.markdown(
        """
    **Estudo considerando x casas**
    """
    )

    # Reading the dataset
    data = pd.read_csv('data/BHdata.csv')

    # Print it out
    st.dataframe(data)