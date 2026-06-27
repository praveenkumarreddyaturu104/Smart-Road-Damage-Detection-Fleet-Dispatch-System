Smart Road Damage Detection & Fleet Dispatch System
An AI-powered road infrastructure management platform that automatically detects road damages, prioritizes repairs, optimizes fleet dispatch, and visualizes damage locations using interactive maps.

Overview:
Road damage is one of the leading causes of road accidents, vehicle damage, and increased maintenance costs. Traditional road inspection methods are time-consuming, expensive, and require manual effort.

This project combines Artificial Intelligence, Computer Vision, Graph Algorithms, and Geospatial Analysis to automate the complete workflow—from detecting road damages to intelligently dispatching repair vehicles using optimized routes.

Features

AI-powered road damage detection using YOLOv8
Detection of:
Potholes
Longitudinal Cracks
Transverse Cracks
Alligator Cracks
Upload and analyze road images
Interactive analytics dashboard
Interactive damage map
Damage heatmap visualization
Intelligent fleet management
GPS-based nearest vehicle allocation
Dijkstra shortest path route optimization
Priority Queue-based repair scheduling
SQLite database integration
Damage statistics and reporting
Modular and scalable architecture



WORKING PROCESS:
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

Technology Stack:
Category	                   Technology
Programming Language	       Python
Deep Learning                YOLOv8
Computer Vision	             OpenCV
Frontend	                   Streamlit
Database	                   SQLite
Mapping	                     Folium
GPS	                         Haversine Formula
Routing                      Dijkstra Algorithm
Scheduling                   Priority Queue (Max Heap)
Data Processing              NumPy, Pandas
Visualization	               Matplotlib

Machine Learning Pipeline:
-->Dataset Preparation
-->XML to YOLO Annotation Conversion
-->Dataset Splitting
-->YOLOv8 Model Training
-->Model Validation
-->Road Damage Detection
-->Database Storage
-->Dashboard Visualization

FLEET DISPATCH PIPLINE:
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
