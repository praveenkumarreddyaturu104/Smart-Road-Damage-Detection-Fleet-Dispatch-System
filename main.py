"""
Main entry point of the project.
"""

# Import settings from config file
from config.settings import (
    IMAGE_WIDTH,
    IMAGE_HEIGHT,
    BATCH_SIZE,
    EPOCHS,
    DATASET_PATH,
    MODEL_PATH,
    DATABASE_NAME
)


def display_project_information():
    """
    Display basic project configuration.
    """

    print("\nRoad Damage Detection System")
    print("-" * 40)

    # Display image dimensions
    print(f"Image Width  : {IMAGE_WIDTH}")
    print(f"Image Height : {IMAGE_HEIGHT}")

    # Display training parameters
    print(f"Batch Size   : {BATCH_SIZE}")
    print(f"Epochs       : {EPOCHS}")

    # Display paths
    print(f"Dataset Path : {DATASET_PATH}")
    print(f"Model Path   : {MODEL_PATH}")

    # Display database name
    print(f"Database     : {DATABASE_NAME}")


def main():
    """
    Start the application.
    """

    print("Starting Road Damage Detection System...")

    # Display configuration details
    display_project_information()

    print("\nSystem initialized successfully.")


# Run program
if __name__ == "__main__":
    main()