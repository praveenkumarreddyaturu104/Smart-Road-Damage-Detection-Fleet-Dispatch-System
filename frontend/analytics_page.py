"""
Analytics page displaying plotly charts of road damage statistics.
"""
import sys
import os
import streamlit as st
import pandas as pd
import plotly.express as px

# Setup project root for absolute imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from database.damage_repository import get_all_damages


def show_analytics_page():
    """
    Load data from the database, compute metrics, and display interactive Plotly charts.
    """
    st.title("📊 Road Damage Analytics Dashboard")
    st.write("Quantitative overview of logged road damages, severities, types, and detection trends.")

    # Retrieve all records
    records = get_all_damages()

    if not records:
        st.info("No road damage records logged yet. Go to the Upload page to scan road images.")
        return

    # Convert to pandas DataFrame
    df = pd.DataFrame(records)

    # Compute key stats
    total_damages = len(df)
    critical_count = len(df[df["severity"] == "Critical"])
    high_count = len(df[df["severity"] == "High"])
    medium_count = len(df[df["severity"] == "Medium"])
    low_count = len(df[df["severity"] == "Low"])

    # Display KPI metrics cards
    st.subheader("Key Performance Indicators")
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Total Detections", total_damages)
    m2.metric("🚨 Critical Issues", critical_count)
    m3.metric("⚠️ High Severity", high_count)
    m4.metric("🟡 Medium Severity", medium_count)
    m5.metric("🟢 Low Severity", low_count)

    # Split page into layout columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Severity Distribution")
        # Pie chart for severity
        severity_counts = df["severity"].value_counts().reset_index()
        severity_counts.columns = ["Severity", "Count"]
        
        # Consistent color map for Plotly charts
        color_discrete_map = {
            "Critical": "#d9534f",  # Red
            "High": "#f0ad4e",      # Orange
            "Medium": "#f0de4e",    # Yellow
            "Low": "#5cb85c"        # Green
        }
        
        fig_pie = px.pie(
            severity_counts,
            names="Severity",
            values="Count",
            color="Severity",
            color_discrete_map=color_discrete_map,
            hole=0.4,
            title="Detections by Severity Category"
        )
        fig_pie.update_layout(title_x=0.25)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.subheader("Top Damage Types")
        # Bar chart for damage type counts
        type_counts = df["damage_type"].value_counts().reset_index()
        type_counts.columns = ["Damage Type", "Count"]
        
        fig_bar = px.bar(
            type_counts,
            x="Damage Type",
            y="Count",
            color="Damage Type",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            title="Detections by Damage Category"
        )
        fig_bar.update_layout(title_x=0.25, showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)

    # Historical Daily Detections
    st.subheader("📅 Daily Detection Trends")
    # Extract date from timestamp
    df["Date"] = pd.to_datetime(df["timestamp"]).dt.date
    daily_trend = df.groupby("Date").size().reset_index(name="Detections")
    
    fig_line = px.line(
        daily_trend,
        x="Date",
        y="Detections",
        markers=True,
        title="Detections Over Time",
        color_discrete_sequence=["#0288d1"]
    )
    fig_line.update_layout(title_x=0.5)
    st.plotly_chart(fig_line, use_container_width=True)