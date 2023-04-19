import streamlit as st 
import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import numpy as np

st.title("Pubs Finder")
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


data_dir = os.path.join(os.getcwd(), "resources", "data")

data_file_path = os.path.join(data_dir, "open_pubs.csv")
data = pd.read_csv(data_file_path, header= None)

# Read in your dataset with latitude and longitude values

columns = ['id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']

data.columns = columns

data = data.replace('\\N', np.nan)
data['latitude'] = data['latitude'].astype(float)
data['longitude'] = data['longitude'].astype(float)

data = data.dropna()

# Display the map in Streamlit
st.title("UK Map with Pubs")
st.map(data) 

st.write("The above map shows United Kingdom region and pubs available in UK. There are around",len(data['local_authority'].unique()),"local authorities that are having pubs in UK") 
st.write("Top 25 locations having most number of pubs are") 
st.write(data['local_authority'].value_counts()[:25]) 

st.write("Minimum value of UK latitude is", min(data['latitude']),"Maximum value is", max(data['latitude']))
st.write("Minimum value of UK longitude is",min(data['longitude']), ", Maximum value is", max(data['longitude']))




