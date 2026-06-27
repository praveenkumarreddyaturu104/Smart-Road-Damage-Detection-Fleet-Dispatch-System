"""
Convert damage area into severity.
"""


def get_severity_level(area):
    """
    Determine severity level.
    """

    # Small pothole
    if area < 1000:
        return "Low"

    # Medium pothole
    elif area < 5000:
        return "Medium"

    # Large pothole
    elif area < 15000:
        return "High"

    # Very large pothole
    else:
        return "Critical"


if __name__ == "__main__":

    severity = get_severity_level(12000)

    print("Severity:", severity)