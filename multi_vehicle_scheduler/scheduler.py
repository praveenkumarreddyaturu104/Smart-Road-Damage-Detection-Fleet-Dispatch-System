"""
Vehicle scheduler.
"""


def schedule_tasks(
        vehicles,
        damage_list):
    """
    Assign damages to vehicles.
    """

    assignments = []

    for vehicle, damage in zip(
            vehicles,
            damage_list):

        assignments.append(
            (
                vehicle.vehicle_id,
                damage
            )
        )

    return assignments


if __name__ == "__main__":

    vehicles = [
        "Vehicle_1",
        "Vehicle_2"
    ]

    damages = [
        "D101",
        "D102"
    ]

    result = schedule_tasks(
        vehicles,
        damages
    )

    print(result)