# Sample data

import streamlit as st
import pydeck as pdk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import xlabel, ylabel, title
from streamlit import status

path = "C:/Users/ellar/OneDrive - Bentley University/sophomore/fall 24/cs 230/python projects/pythonProject/final project/"
df_sky = pd.read_csv(path + "skyscrapers.csv")

st.title('Height Distribution')

#[DA7] and [DA4]
#sort through the data to drop any values of 0
df_sky = df_sky.drop(df_sky[df_sky['statistics.height' ] == 0].index)
df_sky = df_sky.drop(df_sky[df_sky['statistics.floors above'] == 0].index)
#st.write(df_sky)

#[DA3]
#find the max height of all data
df_max_height = df_sky['statistics.height'].max()
st.success(f"The tallest skyscraper in this dataset is {round(df_max_height,3)} meters!:exploding_head:")

#find the min height
df_min_height = df_sky['statistics.height'].min()
st.success(f"The shortest skyscraper in this dataset is {round(df_min_height,3)} meters! :satisfied:")

#find the average height of all skyscrapers
df_mean_height = df_sky['statistics.height'].mean()
st.success(f"The average height of a skyscraper in this dataset is {round(df_mean_height,3)} meters.:smiley:")



#[DA6] and [VIZ3]
df_1 = pd.pivot_table(data = df_sky, index = 'location.city',
                      values= ['statistics.height', 'statistics.floors above'],
                      aggfunc= 'mean')
df_1.columns = ['Average Height (m)','Average # of Floors']
df_1 = df_1.sort_values(by='Average Height (m)', ascending=False)
st.markdown("### Average Heights and Floors by City")
st.write(df_1)


#bar chart that displays the heights of all the skyscrapers in Boston

df_bos = df_sky[df_sky['location.city'] == "Boston"][['statistics.height']]

#st.write(df_bos)

df_bos.plot(kind= 'bar', color= 'g', xlabel = 'Skyscraper ID', ylabel = 'Height (m)')

title("Heights of Boston Skyscrapers")
st.pyplot()
