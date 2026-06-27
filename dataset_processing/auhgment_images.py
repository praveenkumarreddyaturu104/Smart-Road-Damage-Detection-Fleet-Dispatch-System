"""
Perform image augmentation.
"""

import cv2


def flip_image(image):
    """
    Flip image horizontally.
    """

    # Flip image
    flipped_image = cv2.flip(image, 1)

    return flipped_image


def rotate_image(image):
    """
    Rotate image by 90 degrees.
    """

    rotated_image = cv2.rotate(
        image,
        cv2.ROTATE_90_CLOCKWISE
    )

    return rotated_image


# Test
if __name__ == "__main__":

    image = cv2.imread("dataset/sample.jpg")

    flipped = flip_image(image)

    rotated = rotate_image(image)

    print("Image augmentation completed.")