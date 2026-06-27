"""
Generate priority values.
"""


def get_priority(
        severity_level):
    """
    Return priority score.
    """

    if severity_level == "Critical":

        return 100

    elif severity_level == "High":

        return 80

    elif severity_level == "Medium":

        return 50

    else:

        return 20


if __name__ == "__main__":

    priority = get_priority(
        "Critical"
    )

    print(
        "Priority:",
        priority
    )