"""
Preprocess images before training.
"""

import cv2


def preprocess_image(image_path, width=224, height=224):
    """
    Read and resize image.

    Parameters:
        image_path (str): Image location.
        width (int): Width of image.
        height (int): Height of image.

    Returns:
        resized_image
    """

    # Read image
    image = cv2.imread(image_path)

    # Resize image
    resized_image = cv2.resize(image, (width, height))

    return resized_image


# Test
if __name__ == "__main__":

    image_path = "dataset/sample.jpg"

    image = preprocess_image(image_path)

    print("Image shape:", image.shape)