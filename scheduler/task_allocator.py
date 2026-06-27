"""
Allocate repair tasks.
"""


def assign_task(
        vehicle_name,
        damage_id):
    """
    Assign damage to vehicle.
    """

    print(
        vehicle_name,
        "assigned to",
        damage_id
    )


if __name__ == "__main__":

    assign_task(
        "Vehicle_1",
        "D110"
    )