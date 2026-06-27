"""
This file stores common settings used throughout the project.
"""

# Image size for CNN and YOLO models
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224

# Batch size for model training
BATCH_SIZE = 32

# Number of training epochs
EPOCHS = 20

# Path to dataset folder
DATASET_PATH = "dataset"

# Path to save trained models
MODEL_PATH = "models"

# SQLite database file
DATABASE_NAME = "road_damage.db"

# Map default coordinates
DEFAULT_LATITUDE = 17.3850
DEFAULT_LONGITUDE = 78.4867