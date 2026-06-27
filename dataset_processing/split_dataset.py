"""
Split dataset into train, validation and test sets.
"""

from sklearn.model_selection import train_test_split


def split_data(image_paths):
    """
    Split dataset.

    Returns:
        train_data
        validation_data
        test_data
    """

    # Split into train and remaining data
    train_data, remaining_data = train_test_split(
        image_paths,
        test_size=0.3,
        random_state=42
    )

    # Split remaining data into validation and test
    validation_data, test_data = train_test_split(
        remaining_data,
        test_size=0.5,
        random_state=42
    )

    return train_data, validation_data, test_data


# Test
if __name__ == "__main__":

    sample_images = [
        "img1.jpg",
        "img2.jpg",
        "img3.jpg",
        "img4.jpg",
        "img5.jpg",
        "img6.jpg",
        "img7.jpg",
        "img8.jpg"
    ]

    train_set, validation_set, test_set = split_data(sample_images)

    print("Train Images:", len(train_set))
    print("Validation Images:", len(validation_set))
    print("Test Images:", len(test_set))