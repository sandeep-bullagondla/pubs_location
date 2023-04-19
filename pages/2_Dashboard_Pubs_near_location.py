import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import numpy as np
import math

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs.csv")

st.title("Nearest Pubs location") 


# Read in your dataset with latitude and longitude values
data = pd.read_csv(DATA_PATH, header=None)
columns = ['id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']

data.columns = columns

data = data.replace('\\N', np.nan)
data['latitude'] = data['latitude'].astype(float)
data['longitude'] = data['longitude'].astype(float)

data = data.dropna() 

# User's coordinates
st.write("Enter the Latitude and Longitude values of your coordinates")
user_latitude = st.number_input("Insert the latitude value", min_value= min(data['latitude']), max_value=max(data['latitude']))
user_longitude = st.number_input("Insert the longitude value", min_value= min(data['longitude']), max_value=max(data['longitude']))


# Calculate the Euclidean distance between the user's coordinates and each pub's coordinates
for index, pub in data.iterrows():
    distance = math.sqrt((user_latitude - pub["latitude"]) ** 2 + (user_longitude - pub["longitude"]) ** 2)
    data.at[index, "distance"] = distance

# Sort the list of pubs based on their distance from the user's coordinates
five_pubs = data.sort_values("distance")[:5] 

if st.button("Show 5 nearest pubs"):
    st.write("For the given latitude and longitude values, number of nearest local authority (or) authortities are", len(five_pubs['local_authority'].unique()), "they are") 
    st.table(five_pubs['local_authority'].unique())
    st.write("Map of 5 nearest pubs for given co-ordinates")
    st.map(five_pubs)