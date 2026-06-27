"""
Assign severity score.
"""


def calculate_severity_score(
        confidence,
        damage_area):
    """
    Calculate score using confidence
    and damage area.
    """

    # Convert confidence to percentage
    confidence_score = confidence * 100

    # Combine both values
    final_score = (
        confidence_score +
        damage_area / 100
    )

    return round(final_score, 2)


if __name__ == "__main__":

    score = calculate_severity_score(
        0.92,
        8000
    )

    print("Severity score:", score)