"""
Load image file paths from dataset folder.
"""

import os


def load_dataset(dataset_path):
    """
    Read all image files inside the dataset folder.

    Parameters:
        dataset_path (str): Folder containing images.

    Returns:
        image_paths (list): List containing image file paths.
    """

    image_paths = []

    # Loop through all files in folder
    for file_name in os.listdir(dataset_path):

        # Check image extensions
        if file_name.endswith((".jpg", ".jpeg", ".png")):

            # Create complete file path
            file_path = os.path.join(dataset_path, file_name)

            # Store path in list
            image_paths.append(file_path)

    return image_paths


# Test the function
if __name__ == "__main__":

    dataset_folder = "dataset"

    images = load_dataset(dataset_folder)

    print("Total images found:", len(images))

    # Print first five images
    for image in images[:5]:
        print(image)