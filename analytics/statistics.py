"""
Statistical calculations.
"""


def calculate_statistics(total_damages):
    """
    Return statistics dictionary.
    """

    statistics = {

        "total_damages": len(total_damages)

    }

    return statistics


if __name__ == "__main__":

    damages = [

        "D101",

        "D102",

        "D103"

    ]

    result = calculate_statistics(
        damages
    )

    print(result)