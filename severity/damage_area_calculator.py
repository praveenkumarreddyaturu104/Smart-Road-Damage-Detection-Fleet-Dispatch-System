"""
Calculate damage area.
"""


def calculate_damage_area(
        x1,
        y1,
        x2,
        y2):
    """
    Calculate bounding box area.
    """

    # Calculate width
    width = x2 - x1

    # Calculate height
    height = y2 - y1

    # Calculate area
    area = width * height

    return area


if __name__ == "__main__":

    area = calculate_damage_area(
        100,
        50,
        250,
        200
    )

    print("Damage area:", area)