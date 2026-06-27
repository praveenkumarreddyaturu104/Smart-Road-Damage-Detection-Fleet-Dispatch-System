# Smart Road Damage Detection & Fleet Dispatch System

**An AI-powered road infrastructure management platform that automatically detects road damages, prioritizes repairs, optimizes fleet dispatch, and visualizes damage locations using interactive maps.**

---

# Overview

Road damage is one of the leading causes of road accidents, vehicle damage, and increased maintenance costs. Traditional road inspection methods are slow, expensive, and rely heavily on manual inspection.

This project combines Artificial Intelligence, Computer Vision, Graph Algorithms, and Geospatial Analysis to automate the complete road maintenance workflow—from detecting road damages to intelligently dispatching repair vehicles using optimized routes.

---

# Features

- AI-powered road damage detection using YOLOv8
- Detection of Potholes, Longitudinal Cracks, Transverse Cracks, and Alligator Cracks
- Interactive Streamlit dashboard
- Real-time image upload and damage prediction
- Damage severity analysis
- SQLite database integration
- Interactive map visualization using Folium
- Heatmap generation for damage hotspots
- Intelligent fleet management dashboard
- GPS-based nearest vehicle allocation
- Dijkstra shortest path route optimization
- Priority Queue-based repair scheduling
- Damage analytics and reporting
- Modular and scalable architecture

---

# System Architecture

```text
                 Road Image
                      │
                      ▼
             YOLOv8 Detection Model
                      │
      ┌───────────────┴───────────────┐
      ▼                               ▼
 Damage Detection              Damage Classification
      │
      ▼
 SQLite Database
      │
 ┌────┴─────────────┐
 ▼                  ▼
Analytics       Map Visualization
                     │
             Heatmap Generation
                     │
                     ▼
         Fleet Dispatch Scheduler
                     │
      Priority Queue + GPS Routing
                     │
                     ▼
        Dijkstra Route Optimization
                     │
                     ▼
          Repair Vehicle Assignment
```

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Deep Learning | YOLOv8 |
| Computer Vision | OpenCV |
| Frontend | Streamlit |
| Database | SQLite |
| Data Processing | NumPy, Pandas |
| Visualization | Matplotlib |
| Mapping | Folium |
| GPS | Haversine Formula |
| Routing Algorithm | Dijkstra Algorithm |
| Scheduling | Priority Queue (Max Heap) |
| Version Control | Git & GitHub |

---

# Project Structure

```text
RoadDamageDetectionSystem/
│
├── algorithms/
├── analytics/
├── config/
├── database/
├── dataset_processing/
├── detection/
├── frontend/
├── gps/
├── map_visualization/
├── ml/
├── multi_vehicle_scheduler/
├── reports/
├── road_damage_yolo/
├── scheduler/
├── severity/
├── tests/
│
├── main.py
├── train_yolov8.py
├── requirements.txt
├── road_damage.db
└── README.md
```

---

# Machine Learning Pipeline

1. Dataset Collection
2. Image Annotation
3. XML to YOLO Label Conversion
4. Dataset Splitting
5. YOLOv8 Model Training
6. Model Validation
7. Damage Prediction
8. Database Storage
9. Dashboard Visualization

---

# Fleet Dispatch Pipeline

```text
Road Damage
      │
      ▼
Severity Classification
      │
      ▼
Priority Queue
      │
      ▼
Nearest Available Vehicle
      │
      ▼
GPS Distance Calculation
      │
      ▼
Dijkstra Route Planning
      │
      ▼
Repair Assignment
```

---

# Supported Damage Classes

| Class | Description |
|--------|-------------|
| Pothole | Circular Road Damage |
| Longitudinal Crack | Vertical Road Crack |
| Transverse Crack | Horizontal Road Crack |
| Alligator Crack | Network of Interconnected Cracks |

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/<your-username>/RoadDamageDetectionSystem.git
```

## Navigate to the Project

```bash
cd RoadDamageDetectionSystem
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run frontend/app.py
```

---

# Algorithms Used

- YOLOv8 Object Detection
- Dijkstra Shortest Path Algorithm
- Priority Queue (Max Heap)
- Haversine Distance Calculation
- GPS-Based Vehicle Allocation

---

# Future Enhancements

- Live CCTV Camera Integration
- Drone-Based Road Inspection
- Mobile Application
- Real-Time Traffic API Integration
- Automatic Repair Cost Estimation
- Predictive Road Failure Analysis
- Cloud Deployment
- Multi-City Fleet Coordination
- Multi-Model Damage Detection
- Real-Time Emergency Dispatch

---

# Project Highlights

- Built an end-to-end AI-powered road infrastructure management platform.
- Trained a custom YOLOv8 object detection model for four road damage categories.
- Implemented intelligent fleet dispatch using GPS-based nearest vehicle allocation.
- Optimized repair routes using Dijkstra's shortest path algorithm.
- Integrated SQLite for damage storage and analytics.
- Developed interactive dashboards, maps, and heatmaps using Streamlit and Folium.
- Designed a modular architecture for easy scalability and future feature expansion.

---

# AI-Assisted Development

The frontend interface was developed with assistance from **Antigravity AI** to accelerate UI prototyping and streamline user experience design. The core application logic, machine learning pipeline, database integration, routing algorithms, fleet dispatch system, GPS utilities, analytics modules, and overall software architecture were implemented and integrated within the project.

---

# Author

**Praveen Kumar Reddy Aturu**

Bachelor of Technology (Artificial Intelligence & Machine Learning)

GitHub: https://github.com/praveenkumarreddyaturu104

LinkedIn: *Add your LinkedIn profile here*

---

# License

This project is licensed under the MIT License.
