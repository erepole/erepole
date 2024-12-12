import streamlit as st
import pydeck as pdk
import pandas as pd


path = "C:/Users/ellar/OneDrive - Bentley University/sophomore/fall 24/cs 230/python projects/pythonProject/final project/"
df_sky = pd.read_csv(path + "skyscrapers.csv")
#Map data must contain a column named "latitude" or "lat"
#st.write(df_sky)
#renames the columns as lat and long to use in the maps
df_sky.rename(columns={"location.latitude":"lat", "location.longitude": "lon"}, inplace= True)

#:world_map: is the map emoji
st.title("Skyscraper Map :world_map:")

#[ST3] radio
#[ST4] sidebar
selected_map = st.sidebar.radio("Please select the map", ["Simple", "Scatter", "Custom Icon"])

#pivot table shows the number of skyscrapers per city highest to lowest
st.header(':red[Number of Skyscrapers Per City]')
df_1 = pd.pivot_table(data = df_sky, index = 'location.city',
                      values= ['id'],
                      aggfunc= 'count')
df_1.columns = ['Number of Skyscrapers per City']
df_1 = df_1.sort_values(by='Number of Skyscrapers per City', ascending=False)
st.write(df_1)



if selected_map == "Simple":
    st.title('Simple Map')
    view_state = pdk.ViewState(
        latitude=df_sky["lat"].mean(),  # The latitude of the view center
        longitude=df_sky["lon"].mean(),  # The longitude of the view center
        zoom=1,  # View zoom level
        pitch=0)  # Tilt level
        # The most basic map, st.map(df)  won't get full points on final if only used
    st.map(df_sky)


#[MAP] or [VIZ4]
elif selected_map == "Scatter":

    st.title("Scatterplot Map")
    st.write(":blue[_Roll over the map to see the skyscraper's locations!_]")

    # Create a view of the map: https://pydeck.gl/view.html
    view_state = pdk.ViewState(
        latitude=df_sky["lat"].mean(), # The latitude of the view center
        longitude=df_sky["lon"].mean(), # The longitude of the view center
        zoom=1.75, # View zoom level
        pitch=0) # Tilt level

    # Create a map layer with the given coordinates
    layer1 = pdk.Layer(type = 'ScatterplotLayer', # layer type
                      data=df_sky, # data source
                      get_position='[lon, lat]', # coordinates
                      get_radius=100000, # scatter radius
                      get_color= [150,0,300],   # scatter color
                      pickable=True # work with tooltip
                      )

    # Can create multiple layers in a map
    # For more layer information
    # https://deckgl.readthedocs.io/en/latest/layer.html
    # Line layer https://pydeck.gl/gallery/line_layer.html

    layer2 = pdk.Layer('ScatterplotLayer',
                      data=df_sky,
                      get_position='[lon, lat]',
                      get_radius=40000,
                      get_color=[300,0,200],
                      pickable=True
                      )


   # stylish tool tip: https://pydeck.gl/tooltip.html?highlight=tooltip
    tool_tip = {"html": "Skyscraper Location:<br/> <b>{location.city}, {location.country}</b>",
                "style": { "backgroundColor": "gray",
                            "color": "white"}
              }

    # Create a map based on the view, layers, and tool tip
    map = pdk.Deck(
        map_style='mapbox://styles/mapbox/navigation-day-v1', # Go to https://docs.mapbox.com/api/maps/styles/ for more map styles
        initial_view_state=view_state,
        layers=[ layer1, layer2], # The following layer would be on top of the previous layers
        tooltip= tool_tip
    )

    st.pydeck_chart(map) # Show the map in your app

elif selected_map == "Custom Icon":

    st.title("Icon Map")
    st.write(":blue[_Roll over an icon to see the skyscraper's location_]")

    # Create custom icons
    ICON_URL = "https://upload.wikimedia.org/wikipedia/commons/7/75/Map_marker_icon_%E2%80%93_Nicolas_Mollet_%E2%80%93_Modern_tower_%E2%80%93_Tourism_%E2%80%93_White.png"
    # Get the custom icon online
    #Icon or picture finder: https://commons.wikimedia.org/

    # Format your icon
    icon_data = {
        "url": ICON_URL,
        "width": 100,
        "height": 100,
        "anchorY": 1
        }

    # Add icons to your dataframe
    df_sky["icon_data"]= None
    for i in df_sky.index:
        df_sky.at[i, "icon_data"] = icon_data

    # Create a layer with your custom icon
    icon_layer = pdk.Layer(type="IconLayer",
                           data = df_sky,
                           get_icon="icon_data",
                           get_position='[lon,lat]',
                           get_size=40,
                           pickable=True)

    # Create a view of the map: https://pydeck.gl/view.html
    view_state = pdk.ViewState(
        latitude=df_sky["lat"].mean(),
        longitude=df_sky["lon"].mean(),
        zoom=1.75,
        pitch=0
        )

    # stylish tool tip: https://pydeck.gl/tooltip.html?highlight=tooltip
    tool_tip = {"html": "Skyscraper Location:<br/> <b>{location.city}, {location.country}</b>",
                "style": { "backgroundColor": "gray",
                            "color": "white"}
              }


    icon_map = pdk.Deck(
        map_style='mapbox://styles/mapbox/satellite-v9',
        layers=[icon_layer],
        initial_view_state= view_state,
        tooltip = tool_tip
        )

    st.pydeck_chart(icon_map)
