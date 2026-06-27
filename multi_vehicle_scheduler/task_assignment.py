"""
Task assignment.
"""


def assign_task(
        vehicle,
        damage_id):
    """
    Assign damage to vehicle.
    """

    # Mark vehicle busy
    vehicle.available = False

    print(
        vehicle.vehicle_id,
        "assigned to",
        damage_id
    )