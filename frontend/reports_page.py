"""
Reports page allowing users to generate and download CSV and PDF reports.
"""
import sys
import os
import tempfile
import streamlit as st

# Setup project root for absolute imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from database.damage_repository import get_all_damages
from reports.csv_report import generate_csv_report
from reports.pdf_report import generate_pdf_report


def show_reports_page():
    """
    Render reports options and generate download buttons for CSV and PDF.
    """
    st.title("🖨️ Report Generation Centre")
    st.write("Generate and download formal summaries of all logged road damages.")

    # Retrieve logged damages
    damages = get_all_damages()

    if not damages:
        st.info("No road damage records logged yet. Go to the Upload page to scan road images.")
        return

    st.subheader("Report Export Options")
    st.write(f"Total records to export: **{len(damages)}**")

    # Create layout columns for the two report types
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="border: 1px solid #ccc; padding: 20px; border-radius: 10px; background-color: rgba(255,255,255,0.05);">
                <h3>📊 CSV Data Export</h3>
                <p>Standard raw format containing all logged damage details, confidences, coordinates, and timestamps. Best for spreadsheet imports.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")  # Spacer
        
        # Generate CSV to temporary file and load into memory for download
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_csv:
            csv_path = temp_csv.name
            
        try:
            generate_csv_report(damages, csv_path)
            with open(csv_path, "rb") as f:
                csv_bytes = f.read()
                
            st.download_button(
                label="📥 Download CSV Report",
                data=csv_bytes,
                file_name="damage_report.csv",
                mime="text/csv",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Error generating CSV report: {e}")
        finally:
            try:
                os.remove(csv_path)
            except Exception:
                pass

    with col2:
        st.markdown(
            """
            <div style="border: 1px solid #ccc; padding: 20px; border-radius: 10px; background-color: rgba(255,255,255,0.05);">
                <h3>📄 PDF Executive Report</h3>
                <p>Formal PDF document including executive summary table, formatted metrics, priority colorings, and structured tabular index. Best for printing.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")  # Spacer
        
        # Generate PDF to temporary file and load into memory for download
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            pdf_path = temp_pdf.name
            
        try:
            generate_pdf_report(damages, pdf_path)
            with open(pdf_path, "rb") as f:
                pdf_bytes = f.read()
                
            st.download_button(
                label="📥 Download PDF Executive Report",
                data=pdf_bytes,
                file_name="damage_report.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Error generating PDF report: {e}")
        finally:
            try:
                os.remove(pdf_path)
            except Exception:
                pass