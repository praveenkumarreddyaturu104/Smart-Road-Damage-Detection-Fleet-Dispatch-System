"""
Emergency scheduling.
"""


def is_emergency(
        severity_score):
    """
    Check whether damage is emergency.
    """

    if severity_score >= 250:

        return True

    return False


if __name__ == "__main__":

    result = is_emergency(
        300
    )

    print(
        "Emergency:",
        result
    )