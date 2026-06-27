"""
Upload page for road damage detection.
"""
import sys
import os
import tempfile
import random
import cv2
import streamlit as st

# Setup project root for absolute imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from ml.yolo_detector import YOLODetector
from database.damage_repository import insert_damage


def show_upload_page():
    """
    Display the upload page, execute object detection, calculate severity,
    persist findings in database, and render annotated results.
    """
    st.title("🚧 Road Damage Detection & Ingestion")
    st.write("Upload an image of a road to run AI detection, classify severity, and log details.")

    uploaded_file = st.file_uploader(
        "Select Road Image...",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        # Create columns to display original and processed images side by side
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(
                uploaded_file,
                caption="Uploaded Image",
                use_container_width=True
            )

        # Save to temp file so YOLO and CV2 can read it
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(uploaded_file.getvalue())
            image_path = temp_file.name

        # Load image with OpenCV to get real dimensions and draw bounding boxes
        cv_img = cv2.imread(image_path)
        if cv_img is None:
            st.error("Error reading the image file.")
            return

        height, width, _ = cv_img.shape

        # Initialize detector
        detector = YOLODetector()

        with st.spinner("Processing image through YOLOv8..."):
            # Run detection
            results = detector.detect(image_path)
            # Extract detections (either real or simulated fallback)
            detections = detector.extract_detections(results, image_width=width, image_height=height)

        st.success(f"Ingestion complete: Found {len(detections)} issues.")

        # Severity color mapping (BGR format for OpenCV)
        severity_colors = {
            "Critical": (0, 0, 255),    # Red
            "High": (0, 127, 255),      # Orange
            "Medium": (0, 255, 255),    # Yellow
            "Low": (0, 255, 0)          # Green
        }

        # Keep track of calculations for display
        detailed_records = []

        # Draw boxes and save records
        for i, det in enumerate(detections):
            damage_type = det["damage_type"]
            confidence = det["confidence"]
            x1, y1, x2, y2 = det["box"]

            # Calculate box area and determine severity
            area = (x2 - x1) * (y2 - y1)
            if area >= 15000:
                severity = "Critical"
            elif area >= 5000:
                severity = "High"
            elif area >= 1000:
                severity = "Medium"
            else:
                severity = "Low"

            # Generate random GPS coordinates in Hyderabad area
            latitude = round(random.uniform(17.3500, 17.4300), 5)
            longitude = round(random.uniform(78.4300, 78.5300), 5)

            # Insert into database
            insert_damage(
                image_name=uploaded_file.name,
                damage_type=damage_type,
                confidence=confidence,
                severity=severity,
                latitude=latitude,
                longitude=longitude
            )

            detailed_records.append({
                "damage_type": damage_type,
                "confidence": confidence,
                "area": area,
                "severity": severity,
                "latitude": latitude,
                "longitude": longitude
            })

            # Draw rectangle
            color = severity_colors.get(severity, (255, 255, 255))
            cv2.rectangle(cv_img, (x1, y1), (x2, y2), color, 3)

            # Add label
            label = f"{damage_type} ({severity})"
            # Draw a filled background for label readability
            label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            y_label_start = max(y1, label_size[1] + 10)
            cv2.rectangle(
                cv_img,
                (x1, y_label_start - label_size[1] - 5),
                (x1 + label_size[0], y_label_start + base_line - 5),
                color,
                cv2.FILLED
            )
            cv2.putText(
                cv_img,
                label,
                (x1, y_label_start - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 0),  # Black text
                1,
                cv2.LINE_AA
            )

        # Convert processed BGR image to RGB and display it
        rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        with col2:
            st.subheader("Detections & Severity Analysis")
            st.image(
                rgb_img,
                caption="YOLOv8 & Severity Annotation",
                use_container_width=True
            )

        # Display detection details in an expander
        with st.expander("Show Ingested Record Details", expanded=True):
            for i, rec in enumerate(detailed_records):
                st.markdown(
                    f"**Issue #{i+1}: {rec['damage_type']}**  \n"
                    f"* Confidence: `{rec['confidence']*100:.1f}%` | "
                    f"Box Area: `{rec['area']} px²` | "
                    f"Severity: **{rec['severity']}** | "
                    f"GPS Location: `({rec['latitude']}, {rec['longitude']})`"
                )

        # Cleanup temp file
        try:
            os.remove(image_path)
        except Exception:
            pass