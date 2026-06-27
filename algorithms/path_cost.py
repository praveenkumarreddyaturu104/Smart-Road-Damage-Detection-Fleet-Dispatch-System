"""
Calculate route cost.
"""


def calculate_cost(
        distance,
        fuel_rate):
    """
    Calculate total cost.
    """

    # Calculate travel cost
    total_cost = (
        distance * fuel_rate
    )

    return total_cost


if __name__ == "__main__":

    distance = 12

    fuel_rate = 8

    cost = calculate_cost(
        distance,
        fuel_rate
    )

    print(
        "Travel cost:",
        cost
    )