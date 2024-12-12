'''
Ella Repole
CS230
Final Project
Skyscrapers
'''

import streamlit as st
import pydeck as pdk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit import status

path = "C:/Users/ellar/OneDrive - Bentley University/sophomore/fall 24/cs 230/python projects/pythonProject/final project/"
df_sky = pd.read_csv(path + "skyscrapers.csv")

#filters the status
df_status = df_sky["status.current"]
#st.write(df_materials)

st.title("Status")

status_list = df_status

# Count the occurrences of each material
status_counts = {}
for status in status_list :
    if status in status_counts:
        status_counts[status] += 1
    else:
        status_counts[status] = 1

#st.write(material_counts)

#[DA5]
#this table uses & to use two filters to represent a table
st.header("This table represents the number of skyscrapers that are made out of the material "
          "composite and are also under construction.")
df_material = df_sky[(df_sky['material'] == 'composite') &
                     (df_sky['status.current'] == 'under construction')]
st.write(df_material)

#convert status to series to use in the pie chart
status_series = pd.Series(status_counts)

#[VIZ2]
# Create the bar chart using .plot()
status_series.plot(kind='pie',  pctdistance=0.75, labeldistance=1.2)

#I decided to not use the autopct, since some of the slices were so small, it made it hard to see
#autopct='%1.1f%%'
# Add labels and title
#plt.xlabel('Status')
#plt.ylabel('Count')
plt.title('The Distribution of Different Statuses')
# Display the bar chart in Streamlit
st.pyplot()














