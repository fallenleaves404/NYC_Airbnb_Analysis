import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st
import data

data = data.load_data()



def write():





    st.sidebar.title("Search Filter")
    selection = st.sidebar.slider("Select the Range of Price", 0,500,(0,100))
    neighbourhood = st.sidebar.selectbox("Select the Boroughs",("Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island") )


    room_type = st.sidebar.selectbox("Select Types of Rooms",("Entire home/apt", "Private room", "Shared room") )


    data_lager_p = data[data['price'] > int(selection[0])]
    data_low_p = data_lager_p[data_lager_p['price'] < int(selection[1])]
    data_neighbour = data_low_p[data_low_p['neighbourhood_group'] == neighbourhood]
    data_room = data_neighbour[data_neighbour['room_type'] == room_type]

    final_data = data_room



    #The hover_data argument accepts a list of column names to be added to the hover tooltip.
    # The hover_name property controls which column is displayed in bold as the tooltip title

    fig = px.scatter_mapbox(
        final_data,
        hover_data=['price', 'room_type'],
        hover_name= "name",
        color = 'neighbourhood',
        lon = 'longitude',
        lat = 'latitude',
        size  = 'price',
        size_max=10,
        opacity=.70,
        zoom=10,
    )

    fig.layout.mapbox.style = 'stamen-terrain'
    fig.update_layout()

    st.plotly_chart(fig,width = 800,height = 800)