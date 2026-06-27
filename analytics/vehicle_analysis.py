"""
Vehicle analysis.
"""


def vehicle_utilization(
        total_vehicles,
        busy_vehicles):
    """
    Calculate utilization percentage.
    """

    utilization = (

        busy_vehicles /
        total_vehicles

    ) * 100

    return round(
        utilization,
        2
    )


if __name__ == "__main__":

    result = vehicle_utilization(
        10,
        4
    )

    print(
        "Utilization:",
        result
    )