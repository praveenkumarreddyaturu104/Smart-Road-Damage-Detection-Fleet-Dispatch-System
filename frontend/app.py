"""
Main Streamlit application entry point.
"""
import sys
import os
import streamlit as st

# Setup project root for absolute imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from frontend.sidebar import create_sidebar
from frontend.home_page import show_home_page
from frontend.upload_page import show_upload_page
from frontend.history_page import show_history_page
from frontend.map_page import show_map_page
from frontend.analytics_page import show_analytics_page
from frontend.routing_page import show_routing_page
from frontend.reports_page import show_reports_page
from frontend.vehicle_page import show_vehicle_page

# Set page configurations
st.set_page_config(
    page_title="Road Damage Prioritization System",
    page_icon="🚧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Render navigation sidebar
selected_page = create_sidebar()

# Page routing
if selected_page == "🏠 Home":
    show_home_page()
    
elif selected_page == "📤 Upload":
    show_upload_page()
    
elif selected_page == "📋 History":
    show_history_page()
    
elif selected_page == "🗺️ Map":
    show_map_page()
    
elif selected_page == "📊 Analytics":
    show_analytics_page()
    
elif selected_page == "🚚 Fleet":
    show_vehicle_page()
    
elif selected_page == "🛣️ Routing":
    show_routing_page()
    
elif selected_page == "🖨️ Reports":
    show_reports_page()