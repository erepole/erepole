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

path = "C:/Users/ellar/OneDrive - Bentley University/sophomore/fall 24/cs 230/python projects/pythonProject/final project/"
df_sky = pd.read_csv(path + "skyscrapers.csv")

#filter the materials
df_materials = df_sky["material"]
#st.write(df_materials)

st.title("Materials:rock:")

#font is gray and in italics
st.header(":gray[_Skyscrapers can be made out of a lot of different materials. Learn more below!_]")

materials = df_materials

# Count the occurrences of each material
material_counts = {}
for material in materials:
    if material in material_counts:
        material_counts[material] += 1
    else:
        material_counts[material] = 1

#st.write(material_counts)

#[ST2]
#select box to display count of skyscrapers per material
material_select = st.selectbox("These are all the materials that a skyscraper can be made out of. "
                          "Please select a material: ", material_counts)
#displays the type of material
st.write(f"The material you picked from the radio is {material_select}.")
#displays the number of skyscrapers made from that material
st.write(f"There are {material_counts[material_select]} skyscrapers made out of that material in this data set.")


#convert materials to series to use in the bar chart
material_series = pd.Series(material_counts)

#[VIZ1]
# Create the bar chart using .plot()
material_series.plot(kind='bar')

# Add labels and title
plt.xlabel('Materials')
plt.ylabel('Count')
plt.title('Count of Each Material')
# Display the bar chart in Streamlit
st.pyplot()



