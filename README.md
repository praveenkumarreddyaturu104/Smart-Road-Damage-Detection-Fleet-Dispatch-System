Smart Road Damage Detection & Fleet Dispatch System

Tech Stack: Python, YOLOv8, Streamlit, SQLite, OpenCV, Folium, Dijkstra Algorithm, GPS, Priority Queue, Haversine Formula.

---->Developed an AI-powered road damage detection system using YOLOv8 to identify potholes, longitudinal cracks, transverse cracks, and alligator cracks from road images.
---->Built a complete data preprocessing pipeline to convert Pascal VOC XML annotations into YOLO format, prepare datasets, and automate training workflows.
---->Designed an interactive Streamlit dashboard for uploading images, visualizing detections, monitoring analytics, and managing detected road damages.
---->Integrated SQLite for persistent storage of damage records, vehicle information, repair assignments, and historical maintenance data.
---->Implemented Dijkstra's Algorithm for shortest-path route optimization between repair vehicles and reported road damages.
---->Developed a priority-based fleet dispatch system using a Max Heap Priority Queue to assign repair vehicles based on damage severity and urgency.
---->Implemented GPS-based nearest vehicle allocation using the Haversine distance algorithm to minimize response time.
---->Created an interactive Folium map visualization with damage markers, heatmap overlays, and planned repair routes.
---->Built a modular architecture consisting of 40+ Python modules following separation of concerns, enabling scalable maintenance and future feature expansion.
---->Trained and evaluated custom YOLOv8 models on the RDD2022 (Road Damage Detection) dataset containing approximately 11,000 annotated images.
---->Achieved an end-to-end workflow from image upload → AI detection → database storage → fleet scheduling → route optimization → map visualization.
