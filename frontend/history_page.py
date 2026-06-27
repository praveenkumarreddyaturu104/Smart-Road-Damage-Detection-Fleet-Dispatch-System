"""
History page showing all ingested road damage records.
"""
import sys
import os
import streamlit as st
import pandas as pd

# Setup project root for absolute imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from database.damage_repository import get_all_damages, delete_damage


def show_history_page():
    """
    Render all damages registered in the database in a table format,
    and allow record deletion.
    """
    st.title("📋 Damage Log History")
    st.write("Browse, inspect, and manage all logged road damage incidents.")

    # Retrieve all records
    records = get_all_damages()

    if not records:
        st.info("No road damage records logged yet. Go to the Upload page to scan road images.")
        return

    # Convert to pandas DataFrame
    df = pd.DataFrame(records)

    # Rename columns for nicer display
    df_display = df.rename(
        columns={
            "id": "ID",
            "image_name": "Source Image",
            "damage_type": "Damage Type",
            "confidence": "Confidence Score",
            "severity": "Severity Level",
            "latitude": "Latitude",
            "longitude": "Longitude",
            "timestamp": "Detected At"
        }
    )

    # Reorder columns for optimal presentation
    columns_order = [
        "ID",
        "Damage Type",
        "Severity Level",
        "Confidence Score",
        "Detected At",
        "Source Image",
        "Latitude",
        "Longitude"
    ]
    df_display = df_display[columns_order]

    # Format confidence score as percentage
    df_display["Confidence Score"] = df_display["Confidence Score"].apply(lambda x: f"{x * 100:.1f}%")

    # Display dataframe
    st.dataframe(df_display, use_container_width=True)

    # Statistics Summary
    total_count = len(records)
    st.write(f"Showing {total_count} records in total.")

    # Record deletion utility
    st.subheader("🗑️ Delete Records")
    col1, col2 = st.columns([1, 3])
    with col1:
        id_to_delete = st.selectbox(
            "Select Record ID to delete:",
            options=[r["id"] for r in records],
            key="delete_id"
        )
    with col2:
        st.write("") # Spacer
        st.write("")
        if st.button("Delete Selected Record", type="primary"):
            delete_damage(id_to_delete)
            st.success(f"Record with ID {id_to_delete} deleted successfully!")
            st.rerun()
