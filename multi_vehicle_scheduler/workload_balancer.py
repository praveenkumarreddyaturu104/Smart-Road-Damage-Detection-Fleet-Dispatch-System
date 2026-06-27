"""
Balance workload.
"""


def balance_workload(
        vehicle_count,
        total_tasks):
    """
    Calculate tasks per vehicle.
    """

    tasks_per_vehicle = (
        total_tasks //
        vehicle_count
    )

    return tasks_per_vehicle


if __name__ == "__main__":

    result = balance_workload(
        4,
        20
    )

    print(
        "Tasks per vehicle:",
        result
    )