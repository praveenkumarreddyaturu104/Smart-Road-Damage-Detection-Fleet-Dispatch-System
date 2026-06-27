"""
Sidebar menu for app navigation.
"""

import streamlit as st


def create_sidebar():
    """
    Display sidebar and return selected page.
    """
    st.sidebar.title("🚧 Nav Center")
    st.sidebar.write("Road Damage Prioritization")

    page = st.sidebar.radio(
        "Select Page",
        [
            "🏠 Home",
            "📤 Upload",
            "📋 History",
            "🗺️ Map",
            "📊 Analytics",
            "🚚 Fleet",
            "🛣️ Routing",
            "🖨️ Reports"
        ]
    )

    return page