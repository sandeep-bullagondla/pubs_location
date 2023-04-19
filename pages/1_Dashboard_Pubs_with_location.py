import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import numpy as np


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

# absolute path of data
DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs.csv")

st.title(" Pubs Based on Local authority") 


# Read in your dataset without column names
data = pd.read_csv(DATA_PATH, header=None)
#column names for data set
columns = ['id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']
#assining column names to columns
data.columns = columns

#replacing missing values with NA
data = data.replace('\\N', np.nan)

#converting latitude and lonitude columns to decimal types
data['latitude'] = data['latitude'].astype(float)
data['longitude'] = data['longitude'].astype(float)

#dropping missing values
data = data.dropna()

# Display the map in Streamlit
st.write("Pubs with Local Authority") 
location = st.selectbox("Select the Local Authority", data['local_authority'].unique()) 
loc_data = data[data['local_authority']==location] 
if st.button("pubs in local authority"):
    st.write('Total number of pubs available in the given location are', len(loc_data))
    st.map(loc_data)

# Display the map in Streamlit
st.write("In the selected local authority there are pubs in ", len(loc_data['postcode'].unique()), " different postcodes")  
postcode = st.selectbox("Select the pub with PostCode at your local authority", loc_data['postcode'].unique()) 
if st.button("pubs in selected postcode"):
    pos_data = loc_data[loc_data['postcode']==postcode]
    st.map(pos_data)



