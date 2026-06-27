"""
Predict damage severity.
"""

from damage_area_calculator import (
    calculate_damage_area
)

from severity_levels import (
    get_severity_level
)

from severity_model import (
    calculate_severity_score
)


def predict_severity(
        x1,
        y1,
        x2,
        y2,
        confidence):
    """
    Predict severity level.
    """

    # Calculate area
    area = calculate_damage_area(
        x1,
        y1,
        x2,
        y2
    )

    # Get severity category
    level = get_severity_level(
        area
    )

    # Calculate score
    score = calculate_severity_score(
        confidence,
        area
    )

    return {
        "area": area,
        "severity_level": level,
        "severity_score": score
    }


if __name__ == "__main__":

    result = predict_severity(
        100,
        50,
        250,
        200,
        0.95
    )

    print(result)