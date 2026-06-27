"""
Vehicle class.
"""


class Vehicle:
    """
    Store vehicle information.
    """

    def __init__(
            self,
            vehicle_id,
            current_location):

        # Store vehicle ID
        self.vehicle_id = vehicle_id

        # Store location
        self.current_location = current_location

        # Vehicle status
        self.available = True

    def display_information(self):
        """
        Print vehicle details.
        """

        print(
            "Vehicle ID:",
            self.vehicle_id
        )

        print(
            "Location:",
            self.current_location
        )

        print(
            "Available:",
            self.available
        )