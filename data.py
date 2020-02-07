
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
sns.set()
@st.cache(persist= True)
def load_data():
    data = pd.read_csv("AB_NYC_2019.csv")
    data['last_review'] = pd.to_datetime(data['last_review'])
    data.isnull().sum().sort_values(ascending=False)
    data['reviews_per_month'] = data['reviews_per_month'].fillna("0")
    first_date = data['last_review'].min()
    data['last_review'] = data['last_review'].fillna(first_date)
    return data
def data_checkbox(df):
    select_col_name = st.multiselect("Select columns", df.columns.to_list())
    new_col = df[select_col_name]
    st.dataframe(new_col)





def write():

    data_pre = load_data()
    st.write(data_pre.head(10))
    data_checkbox(data_pre)
    st.write('## Plot for the dataset')
    st.image("imag/Price less than 90 quantile of total price.png")
    st.image("imag/Price larger than 90 quantile of total price.png")
    st.image("imag/Num of Houses in Diff Boroughs.png")
    st.image("imag/Price Distribution for Diff Boroughs.png")
    st.image("imag/Price Distribution for Diff Room Type.png")