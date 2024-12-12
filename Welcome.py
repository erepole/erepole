'''
Ella Repole
CS230
Final Project
Skyscrapers
Streamlit CLoud URL:
Description: I used multiple charts to display information about the skyscraper data,
             including materials used, height, status, and location.
'''

import streamlit as st
import pydeck as pdk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


path = "C:/Users/ellar/OneDrive - Bentley University/sophomore/fall 24/cs 230/python projects/pythonProject/final project/"
df_sky = pd.read_csv(path + "skyscrapers.csv")

# :office: =building emoji
st.title("Skyscraper Data :office:")

st.header("_Click through the tabs to learn more about skyscrapers!_")

# [ST1]
name= st.text_input("Please enter your name:")
st.write(f"Welcome {name}!:smile:")

#drops snowflakes
st.snow()

from PIL import Image



# Open your image using Image.open(file_path)
image_file=Image.open("C:\\Users\\ellar\\OneDrive - Bentley University\\sophomore\\fall 24\\cs 230\\python projects\\pythonProject\\final project\\skyscraper_image.jpg")

# Show your image using st.image()
st.image(image_file, width=750, caption="Skyscraper")


#the full dataset
st.write(df_sky)




