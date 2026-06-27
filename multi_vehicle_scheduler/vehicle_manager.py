"""
Vehicle manager.
"""


class VehicleManager:

    def __init__(self):

        # Store vehicles
        self.vehicles = []

    def add_vehicle(
            self,
            vehicle):

        self.vehicles.append(
            vehicle
        )

    def get_available_vehicles(
            self):
        """
        Return available vehicles.
        """

        available_vehicles = []

        for vehicle in self.vehicles:

            if vehicle.available:

                available_vehicles.append(
                    vehicle
                )

        return available_vehicles