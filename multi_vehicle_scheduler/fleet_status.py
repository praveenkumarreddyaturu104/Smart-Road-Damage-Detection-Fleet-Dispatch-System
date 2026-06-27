"""
Fleet status.
"""


class FleetStatus:

    def __init__(self):

        self.active_vehicles = 0

        self.busy_vehicles = 0

    def update_status(
            self,
            active,
            busy):

        self.active_vehicles = active

        self.busy_vehicles = busy

    def display_status(self):

        print(
            "Active Vehicles:",
            self.active_vehicles
        )

        print(
            "Busy Vehicles:",
            self.busy_vehicles
        )


if __name__ == "__main__":

    fleet = FleetStatus()

    fleet.update_status(
        10,
        3
    )

    fleet.display_status()