"""
Map page displaying logged road damages.
"""
import sys
import os
import streamlit as st
import folium

# Setup project root for absolute imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from database.damage_repository import get_all_damages


def show_map_page():
    """
    Load damage records from the SQLite database and render them on an interactive Folium map.
    """
    st.title("🗺️ Interactive Road Damage Map")
    st.write("Visual distribution of detected road issues. Markers are color-coded by severity.")

    # Retrieve all records
    records = get_all_damages()

    if not records:
        st.info("No road damage records logged yet. Go to the Upload page to scan road images.")
        return

    # Color mapping for severities
    color_map = {
        "Critical": "red",
        "High": "orange",
        "Medium": "yellow",
        "Low": "green"
    }

    # Default coordinates (Hyderabad)
    default_lat = 17.3850
    default_lon = 78.4867

    # Center the map at the average of all locations if records exist
    lats = [r["latitude"] for r in records]
    lons = [r["longitude"] for r in records]
    center_lat = sum(lats) / len(records) if records else default_lat
    center_lon = sum(lons) / len(records) if records else default_lon

    from map_visualization.heatmap_generator import create_heatmap

    # Create toggle
    view_mode = st.radio("Select Map View:", ["Marker View", "Damage Heatmap"], horizontal=True)

    # Create Folium Map
    m = folium.Map(location=[center_lat, center_lon], zoom_start=13, control_scale=True)

    if view_mode == "Marker View":
        # Add markers
        for rec in records:
            color = color_map.get(rec["severity"], "blue")
            
            # HTML styled popup for premium feel
            popup_content = f"""
            <div style="font-family: Arial, sans-serif; font-size: 12px; line-height: 1.5; color: black;">
                <h4 style="margin: 0 0 5px 0; color: #333;">Issue #{rec['id']}</h4>
                <b>Type:</b> {rec['damage_type']}<br>
                <b>Severity:</b> <span style="color: {color if color != 'yellow' else '#d4af37'}; font-weight: bold;">{rec['severity']}</span><br>
                <b>Confidence:</b> {rec['confidence']*100:.1f}%<br>
                <b>Detected At:</b> {rec['timestamp']}<br>
                <b>Coordinates:</b> {rec['latitude']:.5f}, {rec['longitude']:.5f}
            </div>
            """
            
            # Create popup
            popup = folium.Popup(popup_content, max_width=250)
            
            # Add marker to map
            folium.Marker(
                location=[rec["latitude"], rec["longitude"]],
                popup=popup,
                tooltip=f"{rec['damage_type']} ({rec['severity']})",
                icon=folium.Icon(color=color, icon="exclamation-sign")
            ).add_to(m)
            
        # Legend for map
        st.markdown(
            """
            <div style="display: flex; gap: 20px; font-family: sans-serif; font-size: 14px; margin-top: 10px; margin-bottom: 10px;">
                <b>Severity Legend:</b>
                <div style="display: flex; align-items: center; gap: 5px;">
                    <div style="width: 15px; height: 15px; background-color: red; border-radius: 50%;"></div>
                    <span>Critical</span>
                </div>
                <div style="display: flex; align-items: center; gap: 5px;">
                    <div style="width: 15px; height: 15px; background-color: orange; border-radius: 50%;"></div>
                    <span>High</span>
                </div>
                <div style="display: flex; align-items: center; gap: 5px;">
                    <div style="width: 15px; height: 15px; background-color: yellow; border-radius: 50%; border: 1px solid #ccc;"></div>
                    <span>Medium</span>
                </div>
                <div style="display: flex; align-items: center; gap: 5px;">
                    <div style="width: 15px; height: 15px; background-color: green; border-radius: 50%;"></div>
                    <span>Low</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        # Heatmap view
        weight_map = {
            "Critical": 1.0,
            "High": 0.7,
            "Medium": 0.4,
            "Low": 0.1
        }
        heat_data = [[r["latitude"], r["longitude"], weight_map.get(r["severity"], 0.1)] for r in records]
        m = create_heatmap(m, heat_data)

    # Render map in streamlit components
    map_html = m._repr_html_()
    st.components.v1.html(map_html, height=600, scrolling=True)