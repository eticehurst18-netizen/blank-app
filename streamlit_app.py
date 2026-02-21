import streamlit as st
import folium
from streamlit_folium import st_folium
import json

st.title("🗺️ Massachusetts Towns Map")

# Center coordinates for Massachusetts
ma_center = [42.2352, -71.0275]

# Create a folium map
m = folium.Map(location=ma_center, zoom_start=8)

# Load your GeoJSON file
try:
    with open("/workspaces/blank-app/Massachusetts_Municipalities_(Feature_Layer).geojson") as f:
        geojson_data = json.load(f)
    
    # Add GeoJSON to map
    folium.GeoJson(
        geojson_data,
        style_function=lambda x: {
            'fillColor': '#87CEEB',
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.5
        },
        tooltip=folium.GeoJsonTooltip(fields=['TOWN'])
    ).add_to(m)
    
except FileNotFoundError:
    st.error("GeoJSON file not found. Make sure the file is in /workspaces/blank-app/")

# Display map
output = st_folium(m, width=1000, height=600)

if output and output.get("last_clicked"):
    st.success(f"You clicked coordinates: {output['last_clicked']}")import streamlit as st
