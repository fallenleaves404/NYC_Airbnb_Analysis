
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import NY_airbnb
import data
PAGES ={
    "Data" : data,

    "Interact Example": NY_airbnb,

}
def main():
    st.title("Data Exploration on NYC Airbnb data")
    st.sidebar.title("Selection")
    selection = st.sidebar.radio("Select", list(PAGES.keys()))
    page = PAGES[selection]

    with st.spinner(f"Loading Page"):

        page.write()



if __name__ == '__main__':
    main()
