"""
Home page dashboard displaying project highlights and key stats.
"""
import sys
import os
import streamlit as st

# Setup project root for absolute imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from database.damage_repository import get_all_damages


def show_home_page():
    """
    Render project dashboard home page containing welcome banner,
    pipeline flowchart, and summary metrics cards.
    """
    # Stylized banner using custom HTML/CSS
    st.markdown(
        """
        <div style="background-image: linear-gradient(to right, #0288d1, #26c6da); padding: 35px; border-radius: 15px; color: white; margin-bottom: 25px;">
            <h1 style="margin: 0; font-size: 32px; color: white;">🚧 Road Damage Detection & Repair Prioritization</h1>
            <p style="margin: 8px 0 0 0; font-size: 16px; opacity: 0.9;">AI-powered automated inspection, severity classification, and dispatch routing optimization.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Fetch stats
    records = get_all_damages()
    total_damages = len(records)
    critical_count = sum(1 for r in records if r["severity"] == "Critical")
    high_count = sum(1 for r in records if r["severity"] == "High")
    
    # Render Metrics
    st.subheader("📊 System-at-a-Glance KPIs")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    col1.metric("Total Logged Issues", total_damages)
    col2.metric("🚨 Critical Severities", critical_count)
    col3.metric("⚠️ High Severities", high_count)
    col4.metric("📄 Reports Available", "2 (PDF / CSV)")
    col5.metric("🚚 Active Routes", "1 Depot / 5 Sectors")

    st.write("---")

    # Pipeline visualization using custom HTML/CSS cards
    st.subheader("🔄 Automated Processing Pipeline")
    
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; background-color: rgba(2, 136, 209, 0.05); padding: 25px; border-radius: 12px; border: 1px solid rgba(2, 136, 209, 0.15); margin-bottom: 25px; text-align: center; font-family: sans-serif;">
            <div style="flex: 1;">
                <h4 style="margin: 0; color: #0288d1; font-size: 15px;">1. Upload Image</h4>
                <p style="margin: 5px 0 0 0; font-size: 12px; color: #888;">Ingest road photos</p>
            </div>
            <div style="font-size: 24px; color: #0288d1; font-weight: bold; padding: 0 10px;">➔</div>
            <div style="flex: 1;">
                <h4 style="margin: 0; color: #0288d1; font-size: 15px;">2. YOLOv8 Scan</h4>
                <p style="margin: 5px 0 0 0; font-size: 12px; color: #888;">Extract bounding boxes</p>
            </div>
            <div style="font-size: 24px; color: #0288d1; font-weight: bold; padding: 0 10px;">➔</div>
            <div style="flex: 1;">
                <h4 style="margin: 0; color: #0288d1; font-size: 15px;">3. Severity Triage</h4>
                <p style="margin: 5px 0 0 0; font-size: 12px; color: #888;">Classify by box size</p>
            </div>
            <div style="font-size: 24px; color: #0288d1; font-weight: bold; padding: 0 10px;">➔</div>
            <div style="flex: 1;">
                <h4 style="margin: 0; color: #0288d1; font-size: 15px;">4. SQLite Log</h4>
                <p style="margin: 5px 0 0 0; font-size: 12px; color: #888;">Persist record details</p>
            </div>
            <div style="font-size: 24px; color: #0288d1; font-weight: bold; padding: 0 10px;">➔</div>
            <div style="flex: 1;">
                <h4 style="margin: 0; color: #0288d1; font-size: 15px;">5. Map & Route</h4>
                <p style="margin: 5px 0 0 0; font-size: 12px; color: #888;">Plot and optimize paths</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # Guidelines & Walkthrough
    st.subheader("💡 How to Use the System")
    g1, g2, g3 = st.columns(3)
    
    with g1:
        st.markdown(
            """
            #### 1. Ingest Road Scans
            Go to the **Upload** page, drag and drop an image of a road, and the YOLOv8 model will automatically detect damages, classify their size, and save details to the database.
            """
        )
        
    with g2:
        st.markdown(
            """
            #### 2. Visualize & Analyze
            View logged damages on the **Map** page (interactive markers color-coded by urgency) and study trends and statistics on the **Analytics** page.
            """
        )
        
    with g3:
        st.markdown(
            """
            #### 3. Route & Export
            Optimize repair paths visiting multiple damages on the **Routing** page, and download executive CSV or ReportLab PDF documents on the **Reports** page.
            """
        )